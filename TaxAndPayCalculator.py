execfile("ShivaniJobs.py")
execfile("TaxCalculator.py")
tax = tax/100.0
tax = pay*(tax)
remainder = kids - 6
pay = 35
contract_pay = 3*(remainder)
actualPay = pay+contract_pay
ultimatePAY=actualPay*(hoursWorked)-(tax)
if kids == 14:
    print "After Tax Country Meadows --> $" + str(ultimatePAY) 
elif kids == 6:
    print "After Tax Hawthorne --> $" + str(ultimatePAY)
elif kids == 19:
    print "After Tax St. Mary --> $" + str(ultimatePAY)
else:
    print "After Tax 30$" + str(ultimatePAY)

30
