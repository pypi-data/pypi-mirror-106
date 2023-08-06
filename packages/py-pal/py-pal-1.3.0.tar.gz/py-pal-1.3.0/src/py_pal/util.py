import argparse
import logging
import os
import string
from pathlib import Path
from typing import Tuple

import pandas as pd


def set_log_level(level):
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for _logger in loggers:
        _logger.setLevel(level)


def setup_logging(module, level=logging.WARNING):
    logging.basicConfig(level=level)
    logger = logging.getLogger(module)
    logger.setLevel(level)

    console = logging.StreamHandler()
    console.setLevel(level)
    formatter = logging.Formatter('[%(levelname)s, %(module)s, %(funcName)s]: %(message)s')
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger


logger = setup_logging(__name__)


def check_positive(value):
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return int_value


def scale_column(data_frame: pd.DataFrame, scale: float):
    return data_frame.apply(lambda x: x * scale)


def normalize_column(data_frame: pd.DataFrame) -> Tuple[pd.DataFrame, float]:
    _min = data_frame.min()
    _max = data_frame.max()
    div = _max - _min
    if _max == _min:
        div = _max
    logger.debug(f"Normalizing column with factor (x - {_min}) / {div}.")
    return data_frame.apply(lambda x: (x - _min) / div), div


VALID_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)


def escape(filename):
    filename_escaped = ''.join(c for c in filename if c in VALID_CHARS)
    filename_escaped = filename_escaped.replace(' ', '_')
    return filename_escaped


levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}


def get_alt_path(path: Path):
    if path.is_file():
        i = 0
        while True:
            i += 1
            _path, ext = os.path.splitext(path)
            new_path = Path("{}-{}{}".format(_path, str(i), ext))
            if not new_path.is_file():
                return new_path
    return path
