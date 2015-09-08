# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Compensate for leap days. 
# Assume that the birthday and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year. 

from datetime import datetime
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
    return False



def daysInMonth(year,month):
    if month == 1:
        return 31
    if month == 2:
        if isLeapYear(year) == True:
            return 29
        return 28
    if month == 3:
        return 31
    if month == 4:
        return 30
    if month == 5:
        return 31
    if month == 6:
        return 30
    if month == 7:
        return 31
    if month == 8:
        return 31
    if month == 9:
        return 30
    if month == 10:
        return 31
    if month == 11:
        return 30
    if month == 12:
        return 31


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert dateIsAfter(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return (days) 

now = datetime.now()
m1,d1,y1 = input("Enter Birth Month, Day, and Year separated by commas: ")  #Birth_Date
y2,m2,d2 = (now.year, now.month, now.day)# 2014,2,8 #Current_Date
print "You are " + str(daysBetweenDates(y1,m1,d1,y2,m2,d2)) + " days old"
print "Today's date and current time is " + '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

