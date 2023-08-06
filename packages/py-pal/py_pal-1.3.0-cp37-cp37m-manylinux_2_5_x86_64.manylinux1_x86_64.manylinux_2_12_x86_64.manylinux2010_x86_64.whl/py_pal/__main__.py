import argparse
import os
import re
import sys

from py_pal import __version__, settings
from py_pal.analysis.estimator import AllArgumentEstimator, SeparateArgumentEstimator
from py_pal.core import profile_python_file
from py_pal.export import show_function_complexity_plots, write_files
from py_pal.settings import COLUMNS_CLI_OUTPUT
from py_pal.util import set_log_level, levels


def main():
    """Command line entry point."""

    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='one or more Python files, e.g. some_file.py', nargs='+')
    parser.add_argument(
        '-ff',
        '--filter-function',
        type=str,
        help='specify functions to be analysed, per default every function is analysed. Regular expressions are '
             'supported.',
        nargs='?'
    )
    parser.add_argument(
        '-fm',
        '--filter-module',
        type=str,
        help='specify modules to be analysed, per default every module is analysed. Regular expressions are '
             'supported.',
        nargs='?'
    )
    parser.add_argument(
        '-l',
        '--line',
        help='Derive cost functions on the basis of individual lines.',
        action='store_true'
    )
    parser.add_argument(
        '-s',
        '--separate',
        help='Estimate a cost function for each argument of a python function separately.',
        action='store_true'
    )
    parser.add_argument('-o', '--out', type=str, help='Output destination for results and plots.', default='',
                        nargs='?')
    parser.add_argument('-p', '--plot', help='Plot fitted cost functions.', action='store_true')
    parser.add_argument('-v', '--version', help='Print the package version to the output stream.', action='store_true')

    parser.add_argument(
        "--log-level",
        default="warning",
        help="Provide logging level. In the default mode messages with a level of warning or higher are passed to the "
             "standard output stream. Example: --log-level=debug",
        nargs='?'
    ),
    parser.add_argument(
        '--format',
        help=f"Output format. The default output format is {settings.FORMAT_STATISTICS}.",
        choices=list(settings.PandasOutputFormat),
        type=settings.PandasOutputFormat,
        default=settings.FORMAT_STATISTICS,
        nargs='?'
    )

    if len(sys.argv) == 1:
        # Display help message if no argument is supplied.
        parser.print_help(sys.stderr)
        return sys.exit(1)

    args, unknown_args = parser.parse_known_args()

    level = levels.get(args.log_level.lower())
    if level is None:
        raise ValueError(f"log level given: {args.log_level} -- must be one of: {' | '.join(levels.keys())}")
    set_log_level(level)

    if args.version:
        print(__version__)
        return

    settings.OUTPUT_DIR = args.out
    settings.FORMAT_STATISTICS = args.format

    sys.path.insert(0, '.')

    if args.filter_function:
        try:
            re.compile(args.filter_function)
        except re.error:
            raise ValueError("Non valid regex pattern")

    if args.filter_module:
        try:
            re.compile(args.filter_module)
        except re.error:
            raise ValueError("Non valid regex pattern")

    sys.path.insert(0, '.')
    for target in args.target:
        tracer = profile_python_file(target, unknown_args)

        if not tracer:
            raise ValueError("File could not be loaded")

        if args.separate:
            res = SeparateArgumentEstimator(
                tracer.get_call_stats(),
                tracer.get_opcode_stats(),
                per_line=args.line,
                filter_function=args.filter_function,
                filter_module=args.filter_module
            ).export()
        else:
            res = AllArgumentEstimator(
                tracer.get_call_stats(),
                tracer.get_opcode_stats(),
                per_line=args.line,
                filter_function=args.filter_function,
                filter_module=args.filter_module
            ).export()

        if not args.out:
            print(res[COLUMNS_CLI_OUTPUT].to_string())

            if args.plot:
                show_function_complexity_plots(res)

        filename, _ = os.path.splitext(os.path.basename(target))
        write_files(
            res,
            filename,
            save_statistics=args.out,
            save_plot=args.out and args.plot,
            statistics_format=args.format,
            plot_output_dir=args.out,
            statistics_output_dir=args.out
        )


if __name__ == "__main__":
    main()
