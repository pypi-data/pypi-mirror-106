Changelog
=========

What's New in Py-PAL 1.3.0
--------------------------

Command line interface changes:
"""""""""""""""""""""""""""""""
- Renamed -f/--function to -ff/--filter-function
- Added -fm/--filter-module functionality to filter results by module

Py-PAL 1.2.0
------------

- Improved the statistics and plotting output

Command line interface changes:
"""""""""""""""""""""""""""""""
- Deprecated `--save` flag in favor of `-o/--out`
- Renamed `-V/--visualize` to `-p/--plot`
- Change functionality of `-f/--function` from executing and profiling a specific function inside a python file to applying the analysis to a selected function. Regular expressions are suported.

Py-PAL 1.1.0
------------

- Improved Data Collection: The heuristic for determining the size of function arguments has been improved.
- More tests
- More documentation
- More argument generation functions in `py_pal.datagen`
- Replaced command line option --debug with --log-level for more configurable log output

Refactoring
"""""""""""
Project structure changes, overall CLI interface is unchanged.
API changes:

- `py_pal.tracer` moved to `py_pal.data_collection.tracer`
- `py_pal.complexity` and `py_pal.estimator` moved to the `py_pal.analysis` package.
- `py_pal.analysis.estimator.Estimator` now takes call and opcode stats as arguments.

Py-PAL 1.0.0
------------

- More thorough testing from different combinations of requirements and Python versions.
- Bug fixes

Py-PAL 0.2.1
------------

Refactoring
"""""""""""

The `estimator` module was refactored which introduces a slight change to the API.
Classes inheriting from `Estimator` now only specify how to transform the collected data with respect to the arguments
of the function.

Instead of `ComplexityEstimator` you should use the `AllArgumentEstimator` class. Additionally there is the
`SeparateArgumentEstimator` which is experimental.

Py-PAL 0.1.6
------------

More accurate Data Collection
"""""""""""""""""""""""""""""

The `Tracer` is enhanced by measuring builtin function calls with `AdvancedOpcodeMetric`.

Opcodes resembling a function call .e.g `FUNCTION_CALL` are filtered for built in function calls.
If the called function is found in the complexity mapping a synthetic Opcode weight gets assigned.
A builtin function call is evaluated using its argument and a pre-defined runtime complexity e.g. O(n log n) for
`sort()`.

- The feature is enabled by default
- The calculation produces a performance overhead and can be disabled by providing a `OpcodeMetric` instance to the `Tracer`
- The `AdvancedOpcodeMetric` instance assigned to the `Tracer` provides statistics about how many builtin function calls were observed and how many were found in the complexity map

Bugfixes
""""""""
- Cleaning data after normalization introduced wrong data points