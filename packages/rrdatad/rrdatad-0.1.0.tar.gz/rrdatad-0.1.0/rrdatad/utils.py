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


def today():
    return datetime.date.today()


def is_str(s):
    return isinstance(s, six.string_types)


def to_date_str(dt):
    if dt is None:
        return None

    if isinstance(dt, six.string_types):
        return dt
    if isinstance(dt, datetime.datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(dt, datetime.date):
        return dt.strftime("%Y-%m-%d")


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


def to_date(date):
    """
    >>> convert_date('2015-1-1')
    datetime.date(2015, 1, 1)
    >>> convert_date('2015-01-01 00:00:00')
    datetime.date(2015, 1, 1)
    >>> convert_date(datetime.datetime(2015, 1, 1))
    datetime.date(2015, 1, 1)
    >>> convert_date(datetime.date(2015, 1, 1))
    datetime.date(2015, 1, 1)
    """
    if is_str(date):
        if ':' in date:
            date = date[:10]
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, datetime.date):
        return date
    elif date is None:
        return None

    raise ValueError("type error")
