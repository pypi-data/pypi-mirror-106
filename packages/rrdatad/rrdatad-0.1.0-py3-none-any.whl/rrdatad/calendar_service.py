# coding=utf-8
import datetime

from rrdatad.utils.rqLogs import log_info
from rrdatad.tushare_pro import pro
from rrdatad.utils.rqDate_trade import  rq_util_format_date2str


class CalendarService(object):

    all_trade_days = None

    @classmethod
    def fetch_all_trade_days(cls):
        df = pro.trade_cal(exchange='SSE', start_date='19900101', end_date='20991231') #'19900101'
        trade_date = df[df.is_open == 1]['cal_date'].values
        trade_date = list(map(lambda x:  rq_util_format_date2str(x),  trade_date))
        return trade_date


    @classmethod
    def get_trade_days(cls, start_date=None, end_date=None, count=None):
        if start_date and count:
            raise ValueError("start_date 参数与 count 参数只能二选一")
        if not (count is None or count > 0):
            raise ValueError("count 参数需要大于 0 或者为 None")
        end_date = rq_util_format_date2str(end_date)
        if start_date:
            start_date =  rq_util_format_date2str(start_date)
            return [d for d in cls.get_all_trade_days() if start_date <= d <= end_date]
        elif count:
            return [d for d in cls.get_all_trade_days() if d <= end_date][-count:]
        else:
            raise ValueError("start_date 参数与 count 参数必须输入一个")


    @classmethod
    def get_all_trade_days(cls):
        if not cls.all_trade_days:
            data =cls.fetch_all_trade_days()
            cls.all_trade_days = list(data)
        return cls.all_trade_days


    @classmethod
    def get_previous_trade_date(cls,  date):
        """
        返回指定日期的最近一个交易日
        如果该日期是交易日，返回该日期；
        否则，返回该日期的前一个交易日
        """
        if date not in cls.get_all_trade_days():
            temp = filter(lambda item: item < date, cls.all_trade_days)
            temp = list(temp)
            return temp[-1] if temp else date
        return date


    @classmethod
    def get_last_trade_date(cls):
        date = rq_util_format_date2str(datetime.datetime.today())
        return cls.get_previous_trade_date(date)


get_trade_days = CalendarService.get_trade_days
get_all_trade_days = CalendarService.get_all_trade_days
get_previous_trade_date = CalendarService.get_previous_trade_date
get_last_trade_date = CalendarService.get_last_trade_date

log_info(get_trade_days(count=10, end_date='2021-05-19'))