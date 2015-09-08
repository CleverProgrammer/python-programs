baseSalary = input("Enter the yearly salary:")
noOfServiceYears = input("Enter the number of years worked:")
totalSales = input("Enter the number of total sales:")

if noOfServiceYears <= 5:
    bonus = 10 * (noOfServiceYears)
else:
    bonus = 20 * (noOfServiceYears)

if totalSales >= 5000 and totalSales < 10000:
    commission = totalSales * 0.03
if totalSales >= 10000:
    commission = totalSales * 0.06
else:
    commission = 0


paycheck = baseSalary + bonus + commission
print paycheck
