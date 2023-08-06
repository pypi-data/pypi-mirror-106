from enum import Enum


class PandasOutputFormat(Enum):
    CSV = 'csv'
    HTML = 'html'
    JSON = 'json'

    def __str__(self):
        return self.value


OUTPUT_DIR = 'stats'
FORMAT_STATISTICS = PandasOutputFormat.CSV
FORMAT_PLOT = 'png'
ENV_SAVE_PLOTS = 'PYPAL_SAVE_PLOTS'
ENV_SAVE_STATISTICS = 'PYPAL_SAVE_STATISTICS'


class Columns:
    """Column names for the :class:`pandas.DataFrame` objects used in the :class:`py_pal.analysis.estimator.Estimator`
    classes."""
    CALL_ID = 'CallID'
    FILE = 'File'
    FUNCTION_NAME = 'FunctionName'
    ARGS_PROXY = 'ArgsProxy'
    ARGS_NAMES = 'Args'
    KWARGS_PROXY = 'KwargsProxy'
    KWARGS_NAMES = 'Kwargs'
    VARARGS_PROXY = 'VarArgsProxy'
    VARARGS_NAMES = 'VarArgs'
    VARKW_PROXY = 'VarKwProxy'
    VARKW_NAMES = 'VarKw'
    LINE = 'Line'
    FUNCTION_LINE = 'FunctionLine'
    OPCODE_WEIGHT = 'OpcodeWeight'
    NORM_OPCODE_WEIGHT = 'NormOpcodeWeight'
    NORM_OPCODE_SCALE = 'NormOpcodeScale'
    ARG_DEP = 'DependentArgs'
    COMPLEXITY = 'Complexity'
    DATA_POINTS = 'DataPoints'
    TRACING_DATA = 'TracingData'
    FUNCTION_ID = 'FunctionID'
    SELECTED_ARG_VALUE = 'Mean'


COLUMNS_ESTIMATOR_INPUT_CALLS = [
    Columns.CALL_ID, Columns.FUNCTION_ID, Columns.FILE, Columns.FUNCTION_LINE, Columns.FUNCTION_NAME,
    Columns.ARGS_NAMES, Columns.ARGS_PROXY, Columns.KWARGS_NAMES, Columns.KWARGS_PROXY, Columns.VARARGS_NAMES,
    Columns.VARARGS_PROXY, Columns.VARKW_NAMES, Columns.VARKW_PROXY,
]
COLUMNS_ESTIMATOR_INPUT_OPCODES = [Columns.CALL_ID, Columns.LINE, Columns.OPCODE_WEIGHT]

COLUMNS_ESTIMATOR_ANALYZE = [
    Columns.FILE, Columns.FUNCTION_LINE, Columns.FUNCTION_NAME, Columns.ARG_DEP, Columns.COMPLEXITY,
    Columns.DATA_POINTS, Columns.TRACING_DATA, Columns.NORM_OPCODE_SCALE
]
COLUMNS_DATAFRAME_OUTPUT = [
    Columns.FUNCTION_NAME, Columns.ARG_DEP, Columns.COMPLEXITY, Columns.FUNCTION_LINE, Columns.FILE,
    Columns.DATA_POINTS, Columns.TRACING_DATA, Columns.NORM_OPCODE_SCALE
]
COLUMNS_CLI_OUTPUT = [
    Columns.FUNCTION_NAME, Columns.ARG_DEP, Columns.COMPLEXITY, Columns.FUNCTION_LINE, Columns.FILE,
    Columns.DATA_POINTS
]
COLUMNS_WRITE_OUTPUT = [
    Columns.FUNCTION_NAME, Columns.ARG_DEP, Columns.COMPLEXITY, Columns.FUNCTION_LINE, Columns.NORM_OPCODE_SCALE,
    Columns.DATA_POINTS, Columns.FILE, Columns.TRACING_DATA,
]
