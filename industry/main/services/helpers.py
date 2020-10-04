import datetime
from datetime import timedelta

def datetime_calendar(from_date, to_date, delta):
    """
    Arguments:
        from_date {datetime.datetime} -- start_date
        to_date {datetime.datetime} -- end_date
        timedelta {datetime.timedelta} -- delta/step of time
    
    Returns:
        list -- list of datetime in intervals
    """

    if to_date-from_date < timedelta(days=0):
        # go back if it's True
        delta *= -1

    time_interval = []
    while from_date <= to_date:
        time_interval.append(from_date)
        from_date += delta
    return time_interval

