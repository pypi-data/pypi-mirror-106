import datetime as dt


"""
datetime manipulations
"""


def string_to_datetime(dates):
    """
    :param dates: List of dates in string format
    :return: List of dates in datetime format
    """
    return [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]


def datetime_to_string(dt_objs, format='%Y-%m-%d'):
    """
    :param dt_objs: List of dates in datetime format
    :param format: Date format to create date strings
    :return: List of dates in string format, following the given format
    """
    return [dt.datetime.strftime(d, format) for d in dt_objs]


def datetime_to_days(dates, year_0=1979):
    """
    :param dates: List of dates in datetime format
    :param year_0: Year from which dates are referenced (literally "year 0")
    :return: List of dates in number of days since "year 0"
    """
    _d = []
    for date in dates:
        d = str(date).split('-')
        d = (float(d[0])-year_0)*365 + float(d[1])*30 + float(d[2])
        _d.append(d)
    return _d

