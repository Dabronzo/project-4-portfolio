from datetime import date


def get_diff_days(datatime):
    """Function to get the difference
    between days"""
    future_date = datatime.date()
    today = date.today()

    result = abs(today - future_date).days

    return result

