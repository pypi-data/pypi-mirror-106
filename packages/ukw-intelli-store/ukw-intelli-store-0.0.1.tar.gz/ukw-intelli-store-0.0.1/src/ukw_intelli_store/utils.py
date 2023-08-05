import numpy as np
from datetime import date
from datetime import datetime as dt

def filter_time(col_data, _from: date = None, _to: date = None):
    """Expects pd.Series in date format. Returns numpy array of shape (len(col_data)) and dtype bool. Values are true if within and false if outside of range.

    Args:
        col_data (pd.Series(dtype = date)): Seies of dates
        _from (dt.date, optional): Start of date range. Defaults to 01.01.2020.
        _to (dt.date, optional): End of date range. Defaults to current date.

    Returns:
        np.array: array of same len. May be used as index selector.
    """
    if _from == None:
        _from = date(2020, 1, 1)
    if _to == None:
        _to = dt.now().date()

    return np.array(col_data > _from) * np.array(col_data < _to)