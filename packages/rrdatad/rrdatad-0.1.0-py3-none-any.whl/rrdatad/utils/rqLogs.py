# Coding:utf-8

import logging

"""2019-01-03  升级到warning级别 不然大量别的代码的log会批量输出出来
2020-02-19 默认使用本地log 不再和数据库同步
"""
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
    

if __name__ == "__main__":
    log_info('test_info')
    log_debug("test warning")
    log_expection('expection')
    
    