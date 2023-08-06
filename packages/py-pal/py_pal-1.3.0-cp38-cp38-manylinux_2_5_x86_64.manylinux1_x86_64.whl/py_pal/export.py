import os
from pathlib import Path

import pandas as pd
from matplotlib import pyplot as plt

from py_pal import settings
from py_pal.analysis.complexity import Complexity
from py_pal.settings import COLUMNS_WRITE_OUTPUT, Columns
from py_pal.util import scale_column, escape, get_alt_path


def plot_data_points(data_frame):
    # Add subplot
    plt.cla()

    tracing_data = data_frame[Columns.TRACING_DATA]
    current_axis = plt.gca()
    x_axis = tracing_data.columns[0]
    tracing_data[Columns.NORM_OPCODE_WEIGHT] = scale_column(
        tracing_data[Columns.NORM_OPCODE_WEIGHT],
        data_frame[Columns.NORM_OPCODE_SCALE]
    )
    tracing_data.plot(
        x=x_axis,
        y=Columns.NORM_OPCODE_WEIGHT,
        kind='scatter',
        title="Function: {}, Args: {}".format(data_frame[Columns.FUNCTION_NAME], data_frame[Columns.ARG_DEP]),
        ax=current_axis,
    )
    x_values = tracing_data[x_axis].to_numpy()
    complexity = data_frame[Columns.COMPLEXITY]
    current_axis.plot(
        x_values,
        scale_column(pd.DataFrame(complexity.compute(x_values)), data_frame[Columns.NORM_OPCODE_SCALE]).to_numpy(),
        color='red'
    )
    return plt


def write_statistics(data_frame: pd.DataFrame, filename: str, output_dir: str = settings.OUTPUT_DIR,
                     format: settings.PandasOutputFormat = settings.FORMAT_STATISTICS):
    stat_data_dir = os.path.join(output_dir, f"{filename}_data")
    if not os.path.exists(stat_data_dir):
        os.makedirs(stat_data_dir)

    kwargs = {}
    if format == settings.PandasOutputFormat.CSV:
        kwargs = dict(sep=";")

    stats_ref_column = []
    for index, row in data_frame.iterrows():
        _filename = "{}_{}_{}.{}".format(
            row[Columns.FUNCTION_NAME],
            row[Columns.ARG_DEP],
            index,
            format.value
        )
        filename_escaped = escape(_filename)
        stats_data_path = get_alt_path(Path(stat_data_dir) / filename_escaped)
        getattr(row[Columns.TRACING_DATA], f'to_{str(format.name).lower()}')(get_alt_path(stats_data_path), **kwargs)
        stats_ref_column.append(stats_data_path)

    data_frame[Columns.TRACING_DATA] = stats_ref_column
    stats_path = Path(output_dir) / "{}.{}".format(filename, format.value)
    ordered_df = data_frame[COLUMNS_WRITE_OUTPUT]
    getattr(ordered_df, f'to_{str(format.name).lower()}')(get_alt_path(stats_path), **kwargs)


def write_plots(original_df, filename: str, output_dir=settings.OUTPUT_DIR, plot_format=settings.FORMAT_PLOT):
    plot_dir = os.path.join(output_dir, f"{filename}_plots")
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    original_df['Plot'] = [""] * len(original_df)
    filtered_df = original_df[[isinstance(x, Complexity) for x in original_df[Columns.COMPLEXITY]]]

    for index, filtered_df in filtered_df.iterrows():
        _filename = "{}_{}_{}.{}".format(
            filtered_df[Columns.FUNCTION_NAME],
            filtered_df[Columns.ARG_DEP],
            index,
            plot_format
        )
        filename_escaped = escape(_filename)
        plot = plot_data_points(filtered_df)
        plot_path = get_alt_path(Path(plot_dir) / filename_escaped)
        plot.savefig(plot_path)
        original_df.iloc[index, -1] = plot_path


def show_function_complexity_plots(res, show=True):
    res = res[[isinstance(x, Complexity) for x in res[Columns.COMPLEXITY]]]
    for index, data_frame in res.iterrows():
        plot = plot_data_points(data_frame)
        if show:
            plot.draw()
    return res


def write_files(df, target, save_statistics=False, statistics_output_dir=None,
                statistics_format=settings.FORMAT_STATISTICS, save_plot=False, plot_output_dir=None,
                plot_format=settings.FORMAT_PLOT):
    """Helper function to allow file output configuration via environment variables. Environment variables have the
    highest precedence."""
    env_plot_output_dir = os.getenv(settings.ENV_SAVE_PLOTS)

    if env_plot_output_dir:
        plot_output_dir = env_plot_output_dir
        save_plot = True
    elif not plot_output_dir:
        plot_output_dir = settings.OUTPUT_DIR

    if save_plot:
        write_plots(df, target, output_dir=plot_output_dir, plot_format=plot_format)

    env_statistics_output_dir = os.getenv(settings.ENV_SAVE_STATISTICS)
    if env_statistics_output_dir:
        statistics_output_dir = env_statistics_output_dir
        save_statistics = True
    elif not statistics_output_dir:
        statistics_output_dir = settings.OUTPUT_DIR

    if save_statistics:
        write_statistics(df, target, output_dir=statistics_output_dir, format=statistics_format)
