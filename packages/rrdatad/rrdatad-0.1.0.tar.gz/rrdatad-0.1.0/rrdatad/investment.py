# coding: utf-8

from importlib import import_module
from utils import to_date

class Security(object):
    code = None
    display_name = None
    name = None
    start_date = None
    end_date = None
    type = None
    parent = None

    def __init__(self, **kwargs):
        self.code = kwargs.get("code", None)
        self.display_name = kwargs.get("display_name", None)
        self.name = kwargs.get("name", None)
        self.start_date = to_date(kwargs.get("start_date", None))
        self.end_date = to_date(kwargs.get("end_date", None))
        self.type = kwargs.get("type", None)
        self.parent = kwargs.get("parent", None)

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code


def convert_security(s):
    if isinstance(s, six.string_types):
        return s
    elif isinstance(s, Security):
        return str(s)
    elif isinstance(s, (list, tuple)):
        res = []
        for i in range(len(s)):
            if isinstance(s[i], Security):
                res.append(str(s[i]))
            elif isinstance(s[i], six.string_types):
                res.append(s[i])
            else:
                raise ParamsError("can't find symbol {}".format(s[i]))
        return res
    elif s is None:
        return s
    else:
        raise ParamsError("security's type should be Security or list")




def _get_sql_session():
    from sqlalchemy.orm import scoped_session, sessionmaker
    session = scoped_session(sessionmaker())
    return session


_sql_session = _get_sql_session()
print(_sql_session())

class SqlQuery(import_module("sqlalchemy.orm").Query):

    limit_value = None
    offset_value = None

    def limit(self, limit):
        self.limit_value = limit
        return super(SqlQuery, self).limit(limit)

    def offset(self, offset):
        self.offset_value = offset
        return super(SqlQuery, self).offset(offset)


def query(*args, **kwargs):
    return SqlQuery(args, **kwargs).with_session(_sql_session)


class Investment(object):

    def __init__(self, code, exchange):
        self.code = code
        #self.name = name
        self.exchange =exchange

    @property
    def sec_id(self):
        if self.exchange == 'XSHE':
            sec_id = self.code + '.' + self.exchange
        if self.exchange == 'XSHG':
            sec_id = self.code + '.' + self.exchange
        return sec_id


class BarData(Investment):
    def __init__(self, code, exchange):
        super().__init__(code, exchange)
        

class SecType(Investment):

    def __init__(self, code, exchange):
        super().__init__(code, exchange)

    @property
    def sec_type(self):
        invest_id = Investment(self.code, self.exchange).sec_id
        print(invest_id)
        if (invest_id.startswith('000') and invest_id.endswith('XSHG')) or (invest_id.startswith('333') and invest_id.endswith('XSHE')):
            sec_type = 'index'
        if (invest_id.startswith('1')and invest_id.endswith('XSHE'))  or (invest_id.startswith('5')and invest_id.endswith('XSHG')) :
            sec_type = 'fund'
        else:
            sec_type = 'stock'
        return sec_type
                    

if __name__ == '__main__':
    print(SecType('000001', 'XSHG').sec_type)
    print(SecType('150003', 'XSHE').sec_type)

    print(Security(code='300146.XSHE').__str__())
    pass

