import numpy as np
from py_pal.data_collection.opcode_metric cimport AdvancedOpcodeMetric, OpcodeMetric
from py_pal.data_collection.proxy cimport get_input_factor
from py_pal.data_collection.arguments cimport getfullargs

from py_pal.util import setup_logging

logger = setup_logging(__name__)

cdef class TraceEvent:
    CALL = 0
    EXCEPTION = 1
    LINE = 2
    RETURN = 3
    C_CALL = 4
    C_EXCEPTION = 5
    C_RETURN = 6
    OPCODE = 7

cdef class Tracer:
    """Tracing hook manager implemented as Cython extension class :doc:`cython:src/tutorial/cdef_classes`."""
    def __init__(self, OpcodeMetric metric=AdvancedOpcodeMetric(), tuple ignore_modules=()):
        self.blacklist = [
            "py_pal",
            "py_pal.analysis.complexity",
            "py_pal.core",
            "py_pal.datagen",
            "py_pal.analysis.estimator",
            "py_pal.util",
            "py_pal.data_collection.arguments",
            "py_pal.data_collection.metric",
            "py_pal.data_collection.opcode_metric",
            "py_pal.data_collection.proxy",
            "py_pal.data_collection.tracer",
            *ignore_modules
        ]
        self.metric = metric
        self.call_id = 0
        self.calls = [(self.call_id, 0, '__main__', 0, '<module>', None, None, None, None, None, None, None, None)]
        self.opcodes = {}
        self.f_weight_map = {}
        self.call_stack = [(self.call_id, 0)]
        self.call_id += 1

    def __call__(self, FrameType frame, int what, object arg) -> Tracer:
        if frame.f_globals.get('__name__', '') not in self.blacklist:
            # Do not measure inside of tracing machinery
            self.trace()

        return self

    def trace(self) -> Tracer:
        """Install tracing hook."""
        PyEval_SetTrace(<Py_tracefunc> trace_func, <PyObject *> self)
        return self

    def stop(self):
        """Remove tracing hook."""
        PyEval_SetTrace(NULL, NULL)

    cpdef object get_call_stats(self):
        """Return function call statistics.
            
        Returns:
            :class:`numpy.ndarray`: Set of function calls with arguments and meta information.
        """
        return np.asarray(self.calls, dtype=object)

    cpdef get_opcode_stats(self):
        """Return opcode statistics.
    
        Returns:
            :class:`numpy.ndarray`: Map of (function call ids, line) to opcode statistics.
        """
        self.metric.report()
        return np.asarray([(*k, v) for k, v in self.opcodes.items()], dtype=object)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

cdef int last_lineno

cdef int trace_func(Tracer self, FrameType frame, int what, PyObject *arg) except -1:
    """`trace_func` is the central data collection functionality. The function is called for specific events within a
    frame, documented in detail in :meth:`sys.settrace`. All events, except the opcode event, are emitted after the 
    opcode execution. The `call` and `return` events are used to structure the calls into a hierarchy. The function is 
    currently not accessible from Python. It is used by :class:'py_pal.data_collection.tracer.Tracer' as a tracing hook.
    """
    frame.f_trace_opcodes = 1
    frame.f_trace_lines = 0

    global last_lineno

    if frame.f_globals.get('__name__', '') in self.blacklist:
        return 0

    if what == TraceEvent.CALL:
        # Add call as row (module, function, args, kwargs)
        self.call_stack.append((self.call_id, last_lineno))

        PyFrame_FastToLocals(frame)
        args, kwonlyargs, varargs, varkw = getfullargs(frame.f_code)

        self.calls.append(
            (
                self.call_id,
                id(frame.f_code),
                frame.f_code.co_filename,
                frame.f_lineno,
                frame.f_code.co_name,
                args,
                tuple(map(lambda x: get_input_factor(frame.f_locals[x]), args)) if args else None,
                kwonlyargs,
                tuple(map(lambda x: get_input_factor(frame.f_locals[x]), kwonlyargs)) if kwonlyargs else None,
                varargs,
                tuple(map(lambda x: get_input_factor(x), frame.f_locals[varargs])) if varargs else None,
                varkw,
                tuple(map(lambda x: get_input_factor(x), frame.f_locals[varkw].values())) if varkw else None,
            )
        )

        self.call_id += 1
        logger.debug(f"Call: {self.calls[len(self.calls) - 1]}")

    elif what == TraceEvent.RETURN:
        if len(self.call_stack) > 1:
            # Do not pop root call row
            child = self.call_stack.pop()
        else:
            child = self.call_stack[0]

        # Add opcode weight to parent call
        parent = self.call_stack[len(self.call_stack) - 1]
        value = self.f_weight_map.get(child[0], 0)
        parent_weight = self.opcodes.get(parent, 0)
        self.opcodes[parent] = parent_weight + value

        _value = self.f_weight_map.get(parent[0], 0)
        self.f_weight_map[parent[0]] = _value + value
        logger.debug(f"Return call: {child[0]}, opcodes: {value}")

    elif what == TraceEvent.OPCODE:
        # Anything in here should cause minimal overhead
        last_lineno = frame.f_lineno
        metric_value = self.metric.get_value(frame)

        # Save opcode weight per line in current call
        call = self.call_stack[len(self.call_stack) - 1][0]
        key = (call, frame.f_lineno)
        value_line = self.opcodes.get(key, 0)
        self.opcodes[key] = value_line + metric_value

        # Keep track of all opcodes executed within call
        value = self.f_weight_map.get(call, 0)
        self.f_weight_map[call] = value + metric_value

    return 0
