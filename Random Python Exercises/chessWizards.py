#Chess Wizards PayRoll

# $50/hr

# Monday: 1 class, Wednesday: 3 classes

# Paydays: 14th and 30th

from datetime import datetime

now = datetime.now()
salaryPerHour = 50
numberOfClasses = 0

if now.day >= 7 and now.day < 14:
    numberOfClasses = 4

if now.day >= 14 and now.day < 21:
    numberOfClasses = 8

if now.day >= 21 and now.day < 28:
    numberOfClasses = 12

if now.day >= 28 and now.day < 31:
    numberOfClasses = 16
    
def main():    

    moneyBalance = numberOfClasses * salaryPerHour
    print "You Made $" + str(moneyBalance) + "! Congratulations!"

main()

