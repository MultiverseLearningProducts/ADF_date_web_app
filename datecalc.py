'''
Calculates difference between dates and adds/subtracts dates
'''

from datetime import datetime, timedelta

# calculates the difference between two dates in days
def duration(start_date, end_date):
    return abs((end_date - start_date).days)

# calculates a new date, by adding an amount of days to a given date
def when(start_date, days_between):
    return start_date + timedelta(days=days_between)
