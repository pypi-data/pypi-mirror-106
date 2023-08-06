# -*- coding: utf-8 -*-
# BioSTEAM: The Biorefinery Simulation and Techno-Economic Analysis Modules
# Copyright (C) 2020-2021, Yoel Cortes-Pena <yoelcortes@gmail.com>
# 
# This module is under the UIUC open-source license. See 
# github.com/BioSTEAMDevelopmentGroup/biosteam/blob/master/LICENSE.txt
# for license details.
"""
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from biosteam.utils import colors as c, CABBI_wheel
from .utils import style_axis, style_plot_limits, fill_plot, set_axes_labels

__all__ = (
    'plot_montecarlo', 
    'plot_montecarlo_across_coordinate',
    'plot_scatter_points', 
    'plot_spearman', 
    'plot_spearman_1d',
    'plot_spearman_2d',
    'plot_horizontal_line',
    'plot_bars', 
    'plot_vertical_line', 
    'plot_scatter_points',
    'plot_contour_1d', 
    'plot_contour_2d', 
    'plot_contour_single_metric',
    'plot_contour_across_coordinate',
    'plot_contour_2d_curves'
)

def plot_spearman(rhos, top=None, name=None, color_wheel=None, index=None):
    if rhos.shape[1] > 1: 
        return plot_spearman_2d(rhos, top, name, color_wheel=color_wheel, index=index)
    else:
        return plot_spearman_1d(rhos, top, name, color_wheel=color_wheel, index=index)

def plot_spearman_1d(rhos, top=None, name=None, color=None,
                     w=1., s=1., offset=0., style=True, 
                     fig=None, ax=None, sort=True, index=None): # pragma: no coverage
    """
    Display Spearman's rank correlation plot.
    
    Parameters
    ----------
    rhos : pandas.Series
         Spearman's rank correlation coefficients to be plotted.
    top=None : float, optional
        Number of parameters to plot (from highest values).
    
    Returns
    -------
    fig : matplotlib Figure
    ax : matplotlib AxesSubplot
    """
    # Sort parameters for plot
    abs_ = abs
    if index is None: index = rhos.index
    if sort:
        rhos, index = zip(*sorted(zip(rhos, index),
                                  key=lambda x: abs_(x[0])))
    if top:
        rhos = rhos[-top:]
        index = index[-top:]
    
    xranges = [(0, i) for i in rhos]
    yranges = [(offset + s*i, w) for i in range(len(rhos))]
    
    # Plot bars one by one
    if ax is None:
        fig, ax = plt.subplots()
    if color is None: color = c.blue_tint.RGBn
    for x, y in zip(xranges, yranges):
        ax.broken_barh([x], y, facecolors=color,
                       edgecolors=c.blue_dark.RGBn)
    
    if style:
        if name is None: name = rhos.name
        # Plot central line
        plot_vertical_line(0, color=c.neutral_shade.RGBn, lw=1)
        
        xticks = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
        yticks = [i[0]+i[1]/2 for i in yranges]
        ax.set_xlim(-1, 1)
        ax.set_xlabel(f"Spearman's correlation with {name}")
        ax.set_xticks(xticks)
        ax.set_yticks(yticks)
        ax.tick_params(axis='y', right=False, direction="inout", length=4)
        ax.tick_params(axis='x', direction="inout", length=4)
        ax.set_yticklabels(index)
        ax.grid(False)
        ylim = plt.ylim()
        
        ax2 = ax.twinx()
        plt.sca(ax2)
        plt.yticks(yticks, [])
        plt.ylim(*ylim)
        ax2.zorder = 1000
        ax2.tick_params(direction="in")
        
        ax3 = ax.twiny()
        plt.sca(ax3)
        plt.xticks(xticks)
        ax3.zorder = 1000
        ax3.tick_params(direction="in", labeltop=False)
    return fig, ax

def plot_spearman_2d(rhos, top=None, name=None, color_wheel=None, index=None,
                     sort=True): # pragma: no coverage
    """
    Display Spearman's rank correlation plot.
    
    Parameters
    ----------
    rhos : list[pandas.Series]
         Spearman's rank correlation coefficients to be plotted.
    top=None : float, optional
        Number of parameters to plot (from highest values).
    
    Returns
    -------
    fig : matplotlib Figure
    ax : matplotlib AxesSubplot
    """
    rhos = list(reversed(rhos))
    if name is None: name = rhos[0].name
    if index is None: index = rhos[0].index
    if sort:
        values = np.array([i.values for i in rhos])
        rhos_mean = np.abs(values.mean(axis=0))
        indices = [i[0] for i in sorted(enumerate(rhos_mean), key=lambda x: x[1])]
        rhos = [[rho[i] for i in indices] for rho in values]
        index = [index[i] for i in indices]
    N = len(rhos)
    s = N + 1
    if not color_wheel: color_wheel = tuple(CABBI_wheel)
    if N > len(color_wheel):
        raise ValueError("length of `color_wheel` must be equal "
                         "to or greater than the number of columns in `rhos`")
    fig, ax = plt.subplots()
    for i, rho in enumerate(rhos):
        plot_spearman_1d(rho, color=color_wheel[N - i - 1].RGBn, s=s, offset=i,
                         fig=fig, ax=ax, style=False, sort=False, top=False)
    # Plot central line
    yranges = [(s/2 + s*i - 1., 1.) for i in range(len(rhos[0]))]
    plot_vertical_line(0, color=c.neutral_shade.RGBn, lw=1)
    xticks = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
    yticks = [i[0]+i[1]/2 for i in yranges]
    ax.set_xlim(-1, 1)
    ax.set_xlabel(f"Spearman's correlation with {name}")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.tick_params(axis='y', right=False, direction="inout", length=4)
    ax.tick_params(axis='x', direction="inout", length=4)
    ax.set_yticklabels(index)
    ax.grid(False)
    ylim = plt.ylim()
    
    ax2 = ax.twinx()
    plt.sca(ax2)
    plt.yticks(yticks, [])
    plt.ylim(*ylim)
    ax2.zorder = 1000
    ax2.tick_params(direction="in")
    
    ax3 = ax.twiny()
    plt.sca(ax3)
    plt.xticks(xticks)
    ax3.zorder = 1000
    ax3.tick_params(direction="in", labeltop=False)
    return fig, ax

# %% Plot metrics vs coordinate

light_color = c.brown_tint.RGBn
dark_color = c.brown_shade.RGBn

def plot_horizontal_line(y, color='grey', **kwargs): # pragma: no coverage
    """Plot horizontal line."""
    plt.axhline(y=y, color=color, **kwargs) 

def plot_vertical_line(x, color='grey', **kwargs): # pragma: no coverage
    """Plot vertical line."""
    plt.axvline(x=x, color=color, **kwargs) 

def plot_scatter_points(xs, ys, color=dark_color, s=50, zorder=1e6, edgecolor='black', marker='o', **kwargs): # pragma: no coverage
    """Plot scatter points and return patch artist."""
    if xs is None: xs = tuple(range(len(ys)))
    return plt.scatter(xs, ys, marker=marker, s=s, color=color, zorder=zorder, edgecolor=edgecolor, **kwargs) 

def plot_bars(scenarios, ys, colors, edgecolors, labels, positions=None): # pragma: no coverage
    barwidth = 0.50
    N_scenarios = len(scenarios)
    N_labels = len(labels)
    if positions is None: positions = N_labels * np.arange(N_scenarios, dtype=float)
    data = (ys, colors, edgecolors, labels)
    for y, color, edgecolor, label in zip(*data):
        plt.bar(positions, y, barwidth,
                align='center', label=label,
                color=color, edgecolor=edgecolor)
        positions += barwidth
    
    plt.xticks(positions-barwidth*(N_labels+1)/2, scenarios)
    plt.tight_layout()
    plt.legend()

def plot_montecarlo(data, 
                    light_color=light_color,
                    dark_color=dark_color,
                    positions=None,
                    transpose=None): # pragma: no coverage
    """
    Return box plot of Monte Carlo evaluation.
    
    Parameters
    ----------
    data : numpy.ndarray or pandas.DataFrame
        Metric values with uncertainty. Each row represents a sample and 
        each column represents a metric. 
    light_colors : Iterable(numpy.ndarray)
        RGB normalized to 1. Defaults to brown.
    dark_colors : Iterable(numpy.ndarray)
        RGB normalized to 1. Defaults to brown.
    transpose : bool, optional 
        If True, data will be transposed. If False, data will not be transposed. 
        If no values is given, data will be transposed when the number of columns 
        is greater than the number of rows.
    
    Returns
    -------
    bx : Patch
    
    """
    if isinstance(data, pd.DataFrame): data = data.values
    if transpose is None and data.ndim == 2:
        N_rows, N_cols = data.shape
        if N_cols > N_rows: data = data.transpose()
    elif transpose:
        data = data.transpose()
    if not positions:
        if data.ndim == 1: 
            positions = (0,)
        else:
            positions = list(range(data.shape[1]))
    bx = plt.boxplot(x=data, positions=positions, patch_artist=True,
                     widths=0.8, whis=[5, 95],
                     boxprops={'facecolor':light_color,
                               'edgecolor':dark_color},
                     medianprops={'color':dark_color,
                                  'linewidth':1.5},
                     flierprops = {'marker':'D',
                                   'markerfacecolor': light_color,
                                   'markeredgecolor': dark_color,
                                   'markersize':6})
    return bx

def plot_montecarlo_across_coordinate(xs, ys, 
                                      light_color=light_color,
                                      dark_color=dark_color): # pragma: no coverage
    """
    Plot Monte Carlo evaluation across a coordinate.
    
    Parameters
    ----------
    xs : numpy.ndarray(ndim=1)
        Coordinate values for each column in ``ys``.
    ys : numpy.ndarray(ndim=2)
        Metric values with uncertainty. Each row represents a sample and each 
        column represent a metric along the x-coordinate.
    light_color : numpy.ndarray
        RGB normalized to 1. Defaults to brown.
    dark_color : numpy.ndarray
        RGB normalized to 1. Defaults to brown.
    
    Returns
    -------
    percentiles : numpy.ndarray(ndim=2)
        5, 25, 50, 75 and 95th percentiles by row (5 rows total).
    
    """
    q05, q25, q50, q75, q95 = percentiles = np.percentile(ys, [5,25,50,75,95], axis=0)

    plt.plot(xs, q50, '-',
             color=dark_color,
             linewidth=1.5) # Median
    plt.fill_between(xs, q25, q75,
                     color=light_color,
                     linewidth=1.0)
    plt.plot(xs, q05, '-.',
             color=dark_color,
             linewidth=1.0) # Lower whisker
    plt.plot(xs, q95, '-.',
             color=dark_color,
             linewidth=1.0) # Upper whisker
    
    return percentiles
    
def plot_contour_1d(X_grid, Y_grid, data, 
                    xlabel, ylabel, xticks, yticks, 
                    metric_bars, fillblack=True): # pragma: no coverage
    """Create contour plots and return the figure and the axes."""
    n = len(metric_bars)
    assert data.shape == (*X_grid.shape, n), (
        "data shape must be (X, Y, M), where (X, Y) is the shape of both X_grid and Y_grid, "
        "and M is the number of metrics"
    )
    gs_kw = dict(height_ratios=[1, 0.25])
    fig, axes = plt.subplots(ncols=n, nrows=2, gridspec_kw=gs_kw)
    cps = np.zeros([n], dtype=object)
    for i in range(n):
        metric_bar = metric_bars[i]
        ax = axes[0, i]
        plt.sca(ax)
        style_plot_limits(xticks, yticks)
        yticklabels = i == 0
        xticklabels = True
        if fillblack: fill_plot()
        cp = plt.contourf(X_grid, Y_grid, data[:, :, i],
                          levels=metric_bar.levels,
                          cmap=metric_bar.cmap)
        cps[i] = cp
        style_axis(ax, xticks, yticks, xticklabels, yticklabels)
        cbar_ax = axes[1, i]
        plt.sca(cbar_ax)
        cb = metric_bar.colorbar(fig, cbar_ax, cp, shrink=0.8, orientation='horizontal')
        plt.axis('off')
    set_axes_labels(axes[:-1], xlabel, ylabel)
    plt.subplots_adjust(hspace=0.1, wspace=0.1)
    return fig, axes, cps, cb

def plot_contour_2d(X_grid, Y_grid, Z_1d, data, 
                    xlabel, ylabel, xticks, yticks, 
                    metric_bars, Z_label=None,
                    Z_value_format=lambda Z: str(Z),
                    fillblack=True, styleaxiskw=None,
                    label=False): # pragma: no coverage
    """Create contour plots and return the figure and the axes."""
    nrows = len(metric_bars)
    ncols = len(Z_1d)
    assert data.shape == (*X_grid.shape, nrows, ncols), (
        "data shape must be (X, Y, M, Z), where (X, Y) is the shape of both X_grid and Y_grid, "
        "M is the number of metrics, and Z is the number of elements in Z_1d"
    )
    widths = np.ones(ncols + 1)
    widths[-1] /= 4
    gs_kw = dict(width_ratios=widths)
    fig, axes = plt.subplots(ncols=ncols + 1, nrows=nrows, gridspec_kw=gs_kw)
    axes = axes.reshape([nrows, ncols + 1])
    if styleaxiskw is None: styleaxiskw = {}
    cps = np.zeros([nrows, ncols], dtype=object)
    cbs = np.zeros([nrows], dtype=object)
    linecolor = c.neutral_shade.RGBn
    for row in range(nrows):
        metric_bar = metric_bars[row]
        for col in range(ncols):
            ax = axes[row, col]
            plt.sca(ax)
            style_plot_limits(xticks, yticks)
            yticklabels = col == 0
            xticklabels = row == nrows - 1
            if fillblack: fill_plot()
            metric_data = data[:, :, row, col]
            cp = plt.contourf(X_grid, Y_grid, metric_data,
                              levels=metric_bar.levels,
                              cmap=metric_bar.cmap)
            if label:
                cs = plt.contour(cp, zorder=1e16,
                                 linestyles='dashed', linewidths=1.,
                                 levels=cp.levels, colors=[linecolor])
                clabels = ax.clabel(cs, levels=[i for i in cs.levels if i!=metric_bar.levels[-1]], inline=True, fmt=metric_bar.fmt,
                          fontsize=12, colors=['k'], zorder=1e16)
                for i in clabels: i.set_rotation(0)
            cps[row, col] = cp
            style_axis(ax, xticks, yticks, xticklabels, yticklabels, **styleaxiskw)
        cbar_ax = axes[row, -1]
        cbs[row] = metric_bar.colorbar(fig, cbar_ax, cp, shrink=0.8)
        # plt.clim()
    for col in range(ncols):
        if not col and Z_label:
            title = f"{Z_label}: {Z_value_format(Z_1d[col])}"
        else:
            title = Z_value_format(Z_1d[col])
        ax = axes[0, col]
        ax.set_title(title)
    for ax in axes[:, -1]:
        plt.sca(ax)
        plt.axis('off')
    set_axes_labels(axes[:, :-1], xlabel, ylabel)
    plt.subplots_adjust(hspace=0.1, wspace=0.1)
    return fig, axes, cps, cbs
       
def plot_contour_single_metric(X_grid, Y_grid, data, 
                    xlabel, ylabel, xticks, yticks, metric_bar,
                    titles=None, fillblack=True, styleaxiskw=None,
                    label=False): # pragma: no coverage
    """Create contour plots and return the figure and the axes."""
    *_, nrows, ncols = data.shape
    assert data.shape == (*X_grid.shape, nrows, ncols), (
        "data shape must be (X, Y, M, N), where (X, Y) is the shape of both X_grid and Y_grid"
    )
    widths = np.ones(ncols + 1)
    widths[-1] /= 4
    gs_kw = dict(width_ratios=widths)
    fig, axes = plt.subplots(ncols=ncols + 1, nrows=nrows, gridspec_kw=gs_kw)
    axes = axes.reshape([nrows, ncols + 1])
    gs = axes[0, 0].get_gridspec()
    for ax in axes[:, -1]: ax.remove()
    ax_colorbar = fig.add_subplot(gs[:, -1])
    if styleaxiskw is None: styleaxiskw = {}
    cps = np.zeros([nrows, ncols], dtype=object)
    linecolor = c.neutral_shade.RGBn
    for row in range(nrows):
        for col in range(ncols):
            ax = axes[row, col]
            plt.sca(ax)
            style_plot_limits(xticks, yticks)
            yticklabels = col == 0
            xticklabels = row == nrows - 1
            if fillblack: fill_plot()
            metric_data = data[:, :, row, col]
            cp = plt.contourf(X_grid, Y_grid, metric_data,
                              levels=metric_bar.levels,
                              cmap=metric_bar.cmap)
            if label:
                cs = plt.contour(cp, zorder=1e16,
                                 linestyles='dashed', linewidths=1.,
                                 levels=cp.levels, colors=[linecolor])
                clabels = ax.clabel(cs, levels=[i for i in cs.levels if i!=metric_bar.levels[-1]], inline=True, fmt=metric_bar.fmt,
                          fontsize=12, colors=['k'], zorder=1e16)
                for i in clabels: i.set_rotation(0)
            cps[row, col] = cp
            style_axis(ax, xticks, yticks, xticklabels, yticklabels, **styleaxiskw)
    cb = metric_bar.colorbar(fig, ax_colorbar, cp, fraction=nrows * 0.13)
    plt.sca(ax_colorbar)
    plt.axis('off')
    if titles:
        for col, title in enumerate(titles):
            ax = axes[0, col]
            ax.set_title(title)
    set_axes_labels(axes[:, :-1], xlabel, ylabel)
    plt.subplots_adjust(hspace=0.1, wspace=0.1)
    return fig, axes, cps, cb

def plot_contour_2d_curves(X_grid, Y_grid, Z_1d, data, 
                    xlabel, ylabel, xticks, yticks, 
                    metric_bars, Z_label=None,
                    Z_value_format=lambda Z: str(Z),
                    fillblack=True, styleaxiskw=None): # pragma: no coverage
    """Create contour curve plots and return the figure and the axes."""
    nrows = len(metric_bars)
    ncols = len(Z_1d)
    assert data.shape == (*X_grid.shape, nrows, ncols), (
        "data shape must be (X, Y, M, Z), where (X, Y) is the shape of both X_grid and Y_grid, "
        "M is the number of metrics, and Z is the number of elements in Z_1d"
    )
    widths = np.ones(ncols)
    gs_kw = dict(width_ratios=widths)
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, gridspec_kw=gs_kw)
    axes = axes.reshape([nrows, ncols])
    if styleaxiskw is None: styleaxiskw = {}
    cps = np.zeros([nrows, ncols], dtype=object)
    for row in range(nrows):
        metric_bar = metric_bars[row]
        for col in range(ncols):
            ax = axes[row, col]
            plt.sca(ax)
            style_plot_limits(xticks, yticks)
            yticklabels = col == 0
            xticklabels = row == nrows - 1
            if fillblack: fill_plot()
            metric_data = data[:, :, row, col]
            cp = plt.contour(X_grid, Y_grid, metric_data,
                              levels=metric_bar.levels,
                              cmap=metric_bar.cmap)
            clabels = ax.clabel(cp, levels=cp.levels, inline=True, fmt=lambda x: f'{round(x):,}',
                      fontsize=12, colors=['k'], zorder=1e16)
            for i in clabels: i.set_rotation(0)
            cps[row, col] = cp
            style_axis(ax, xticks, yticks, xticklabels, yticklabels, **styleaxiskw)
    for col in range(ncols):
        if not col and Z_label:
            title = f"{Z_label}: {Z_value_format(Z_1d[col])}"
        else:
            title = Z_value_format(Z_1d[col])
        ax = axes[0, col]
        ax.set_title(title)
    for ax in axes[:, -1]:
        plt.sca(ax)
        plt.axis('off')
    set_axes_labels(axes[:, :-1], xlabel, ylabel)
    plt.subplots_adjust(hspace=0.1, wspace=0.1)
    return fig, axes, cps

def plot_contour_across_coordinate(X_grid, Y_grid, Z_1d, data, 
                                   xlabel, ylabel, xticks, yticks, 
                                   metric_bar, Z_label=None,
                                   Z_value_format=lambda Z: str(Z),
                                   fillblack=True): # pragma: no coverage
    """Create contour plots and return the figure and the axes."""
    ncols = len(Z_1d)
    assert data.shape == (*X_grid.shape, ncols), (
        "data shape must be (X, Y, Z), where (X, Y) is the shape of both X_grid and Y_grid, "
        "and Z is the number of elements in Z_1d"
    )
    widths = np.ones(ncols + 1)
    widths[-1] *= 0.38196601125
    gs_kw = dict(width_ratios=widths)
    fig, axes = plt.subplots(ncols=ncols + 1, nrows=1, gridspec_kw=gs_kw)
    xticklabels = True
    for col in range(ncols):
        ax = axes[col]
        plt.sca(ax)
        style_plot_limits(xticks, yticks)
        yticklabels = col == 0
        if fillblack: fill_plot()
        cp = plt.contourf(X_grid, Y_grid, data[:, :, col],
                          levels=metric_bar.levels,
                          cmap=metric_bar.cmap)
        style_axis(ax, xticks, yticks, xticklabels, yticklabels)
    cbar_ax = axes[-1]
    metric_bar.colorbar(fig, cbar_ax, cp, fraction=0.35, pad=0.15)
    for col in range(ncols):
        if not col and Z_label:
            title = f"{Z_label}: {Z_value_format(Z_1d[col])}"
        else:
            title = Z_value_format(Z_1d[col])
        ax = axes[col]
        ax.set_title(title)
    plt.sca(axes[-1])
    style_plot_limits(xticks, yticks)
    plt.axis('off')
    set_axes_labels(axes[np.newaxis, :-1], xlabel, ylabel)
    plt.subplots_adjust(hspace=0.1, wspace=0.1)
    return fig, axes
            
# def plot_contour_across_metric(X_grid, Y_grid, data, 
#                                xlabel, ylabel, xticks, yticks, 
#                                metric_bars, Z_value_format=lambda Z: str(Z),
#                                fillblack=True):
#     """Create contour plots and return the figure and the axes."""
#     ncols = len(metric_bars)
#     assert data.shape == (*X_grid.shape, ncols), (
#         "data shape must be (X, Y, M), where (X, Y) is the shape of both X_grid and Y_grid, "
#         "and M is the number of metric bars"
#     )
#     widths = np.ones(ncols + 1)
#     widths[-1] /= 4
#     gs_kw = dict(width_ratios=widths)
#     fig, axes = plt.subplots(ncols=ncols + 1, nrows=1, gridspec_kw=gs_kw)
#     xticklabels = True
#     for col in range(ncols):
#         ax = axes[col]
#         plt.sca(ax)
#         style_plot_limits(xticks, yticks)
#         yticklabels = col == 0
#         style_axis(ax, xticks, yticks, xticklabels, yticklabels)
#         if fillblack: fill_plot()
#         cp = plt.contourf(X_grid, Y_grid, data[:, :, col],
#                           cmap=metric_bar.cmap)
#     cbar_ax = axes[-1]
#     metric_bar.colorbar(fig, cbar_ax, cp)
#     for col in range(ncols):
#         title = Z_value_format(Z_1d[col])
#         ax = axes[col]
#         ax.set_title(title)
#     plt.sca(axes[-1])
#     plt.axis('off')
#     set_axes_labels(axes[:-1], xlabel, ylabel)
#     plt.subplots_adjust(hspace=0.1, wspace=0.1)
#     return fig, axes
