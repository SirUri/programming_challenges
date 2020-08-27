#==============================================================================
# This is Problem number 19 of https://projecteuler.net/.
# You are given the following information, but you may prefer to do some research 
# for yourself.
# 
# 1 Jan 1900 was a Monday.
# 
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# 
# A leap year occurs on any year evenly divisible by 4, but not on a century unless
#  it is divisible by 400.
#  
# How many Sundays fell on the first of the month during the twentieth century 
# (1 Jan 1901 to 31 Dec 2000)?
#==============================================================================
# Leap year conditions:
#
# 1. evenly divisible by 4
# 
# 2. NOT a leap year if the year is divisible by 100 UNLESS,
# 
# 3. it is divisible by 400
#==============================================================================
#==============================================================================
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthdict = {1: "Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
weekday  = {0:"Monday", 1: "Tuesday", 2: "Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

import time
def isleapyear(year):
    """Determine whether a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def issunday(daysum):
    return daysum % 7 == 6

def problem19(months):
    days = 0
    result = 0
    for year in range(1901, 2001):
        for month in range(len(months)):
            if month == 1 and isleapyear(year):
                for day in range(29):
                    days += 1
                    if issunday(days) and day == 0:
                        result += 1
                        print(day + 1, monthdict[month], year)
            else:
                for day in range(months[month]):
                    days += 1
                    if issunday(days) and day == 0:
                        result += 1
                        print(day + 1, monthdict[month+1], year)
    return result

sundays = problem19(months)
print("Result: %(sundays)s sundays" %locals())