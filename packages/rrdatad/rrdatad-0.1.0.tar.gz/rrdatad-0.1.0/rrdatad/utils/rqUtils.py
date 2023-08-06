# coding=utf-8

import datetime
from functools import wraps
from collections import namedtuple
from importlib import import_module

import six
import pandas as pd

from functools import lru_cache

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
logger.addHandler(console)


def log_debug(logs, ui_log=None, ui_progress=None):
    logging.debug(logs)


def log_info(logs, ui_log=None, ui_progress=None, ui_progress_int_value=None):
    logging.warning(logs)


def log_expection(logs, ui_log=None, ui_progress=None):
    logging.exception(logs)


def is_str(s):
    return isinstance(s, six.string_types)


def is_list(l):
    return isinstance(l, (list, tuple))


def normal_security_code(code):
    """
    :param code:"000001.XSHE"
    :return: "000001"
    """
    if is_str(code):
        if "." in code:
            return code.split(".")[0]
        else:
            return code
    elif is_list(code):
        res = []
        for i in code:
            if "." in i:
                res.append(i.split(".")[0])
            else:
                res.append(i)
        return res
    elif code is None:
        return code
    else:
        raise ValueError("security type is invalid! type is {}".format(type(code)))

