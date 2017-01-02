"""
Problem 19

You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime as dt


def isLeap(year):
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return False
    if (year % 4 == 0):
        return True
    else:
        return False

startDate = dt.date(1901, 1, 1)     #year,month, day
endDate = dt.date(2000, 12, 31)     #year,month, day
increaseInDays = dt.timedelta(days = 1)     #a day value
counter = 0
while (startDate <= endDate):
    if (startDate.day == 1 and startDate.weekday() == 6):   #.weekday = Monday is 0 and Sunday is 6
        counter += 1
    startDate += increaseInDays

print(counter)