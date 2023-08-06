from typing import List, Tuple
import numpy as np

import matplotlib.pyplot as plt

from mikeio import Dfsu

from .observation import Observation, PointObservation, TrackObservation
from .metrics import _linear_regression

def scatter(
    x,
    y,
    binsize: float = None,
    nbins: int = 20,
    show_points: bool = None,
    show_hist: bool = True,
    backend: str = "matplotlib",
    figsize: List[float] = (8, 8),
    xlim: List[float] = None,
    ylim: List[float] = None,
    reg_method: str = "ols",
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    **kwargs,
):
    """Scatter plot showing compared data: observation vs modelled
    Optionally, with density histogram.

    Parameters
    ----------
    x: np.array
        X values e.g model values, must be same length as y
    y: np.array
        Y values e.g observation values, must be same length as x
    binsize : float, optional
        the size of each bin in the 2d histogram, by default None
    nbins : int, optional
        number of bins (if binsize is not given), by default 20
    show_points : bool, optional
        Should the scatter points be displayed?
        None means: only show points if fewer than threshold, by default None
    show_hist : bool, optional
        show the data density as a a 2d histogram, by default True
    backend : str, optional
        use "plotly" (interactive) or "matplotlib" backend, by default "matplotlib"
    figsize : tuple, optional
        width and height of the figure, by default (8, 8)
    xlim : tuple, optional
        plot range for the observation (xmin, xmax), by default None
    ylim : tuple, optional
        plot range for the model (ymin, ymax), by default None
    reg_method : str, optional
        method for determining the regression line
        "ols" : ordinary least squares regression
        "odr" : orthogonal distance regression,
        by default "ols"
    title : str, optional
        plot title, by default None
    xlabel : str, optional
        x-label text on plot, by default None
    ylabel : str, optional
        y-label text on plot, by default None
    model : (int, str), optional
        name or id of model to be compared, by default None
    observation : (int, str), optional
        name or ids of observations to be compared, by default None
    start : (str, datetime), optional
        start time of comparison, by default None
    end : (str, datetime), optional
        end time of comparison, by default None
    area : list(float), optional
        bbox coordinates [x0, y0, x1, y1],
        or polygon coordinates[x0, y0, x1, y1, ..., xn, yn],
        by default None
    df : pd.dataframe, optional
        show user-provided data instead of the comparers own data, by default None
    kwargs
    """

    if len(x) != len(y):
        raise ValueError("x & y are not of equal length")

    if show_points is None:
        show_points = len(x) < 1e4

    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    xymin = min([xmin, ymin])
    xymax = max([xmax, ymax])

    if xlim is None:
        xlim = [xymin, xymax]

    if ylim is None:
        ylim = [xymin, xymax]

    if binsize is None:
        binsize = (xmax - xmin) / nbins
    else:
        nbins = int((xmax - xmin) / binsize)

    xq = np.quantile(x, q=np.linspace(0, 1, num=nbins))
    yq = np.quantile(y, q=np.linspace(0, 1, num=nbins))

    # linear fit
    slope, intercept = _linear_regression(obs=x, model=y, reg_method=reg_method)

    if intercept < 0:
        sign = ""
    else:
        sign = "+"
    reglabel = f"Fit: y={slope:.2f}x{sign}{intercept:.2f}"

    if backend == "matplotlib":

        plt.figure(figsize=figsize)
        plt.plot([xlim[0], xlim[1]], [xlim[0], xlim[1]], label="1:1", c="blue")
        plt.plot(xq, yq, label="Q-Q", c="gray")
        plt.plot(
            x,
            intercept + slope * x,
            "r",
            label=reglabel,
        )
        if show_hist:
            plt.hist2d(x, y, bins=nbins, cmin=0.01, **kwargs)
        plt.legend()
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.axis("square")
        plt.xlim(xlim)
        plt.ylim(ylim)
        if show_hist:
            cbar = plt.colorbar(fraction=0.046, pad=0.04)
            cbar.set_label("# points")
        if show_points:
            plt.scatter(x, y, c="0.25", s=20, alpha=0.5, marker=".", label=None)
        plt.title(title)

    elif backend == "plotly":  # pragma: no cover
        import plotly.graph_objects as go

        data = [
            go.Scatter(
                x=x,
                y=intercept + slope * x,
                name=reglabel,
                mode="lines",
                line=dict(color="red"),
            ),
            go.Scatter(
                x=xlim, y=xlim, name="1:1", mode="lines", line=dict(color="blue")
            ),
            go.Scatter(x=xq, y=yq, name="Q-Q", mode="lines", line=dict(color="gray")),
        ]

        if show_hist:
            data.append(
                go.Histogram2d(
                    x=x,
                    y=y,
                    xbins=dict(size=binsize),
                    ybins=dict(size=binsize),
                    colorscale=[
                        [0.0, "rgba(0,0,0,0)"],
                        [0.1, "purple"],
                        [0.5, "green"],
                        [1.0, "yellow"],
                    ],
                )
            )

        if show_points:
            data.append(
                go.Scatter(
                    x=x,
                    y=y,
                    mode="markers",
                    name="Data",
                    marker=dict(color="black"),
                )
            )

        defaults = {"width": 600, "height": 600}
        defaults = {**defaults, **kwargs}

        layout = layout = go.Layout(
            legend=dict(x=0.01, y=0.99),
            yaxis=dict(scaleanchor="x", scaleratio=1),
            title=dict(text=title, xanchor="center", yanchor="top", x=0.5, y=0.9),
            yaxis_title=ylabel,
            xaxis_title=xlabel,
            **defaults,
        )

        fig = go.Figure(data=data, layout=layout)
        fig.update_xaxes(range=xlim)
        fig.update_yaxes(range=ylim)
        fig.show()  # Should this be here

    else:

        raise ValueError(f"Plotting backend: {backend} not supported")


def plot_observation_positions(
    dfs: Dfsu, observations: List[Observation], figsize: Tuple = None
):
    """Plot observation points on a map showing the model domain

    Parameters
    ----------
    dfs: Dfsu
        model object
    observations: list
        Observation collection
    figsize : (float, float), optional
        figure size, by default None
    """

    xn = dfs.node_coordinates[:, 0]
    offset_x = 0.02 * (max(xn) - min(xn))
    ax = dfs.plot(plot_type="outline_only", figsize=figsize)
    for obs in observations:
        if isinstance(obs, PointObservation):
            ax.scatter(x=obs.x, y=obs.y, marker="x")
            ax.annotate(obs.name, (obs.x + offset_x, obs.y))
        elif isinstance(obs, TrackObservation):
            if obs.n_points < 10000:
                ax.scatter(x=obs.x, y=obs.y, c=obs.values, marker=".", cmap="Reds")
            else:
                print("Too many points to plot")
                # TODO: group by lonlat bin
    return ax
