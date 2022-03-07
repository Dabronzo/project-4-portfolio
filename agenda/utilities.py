from datetime import date


def get_diff_days(datatime):
    """Function to get the difference
    between days"""
    future_date = datatime.date()
    today = date.today()

    result = (future_date - today).days

    return result
