kids = input("Enter the number of kids:")
hoursWorked = input("Enter the number of hours:")
remainder = kids - 6
pay = 35
contract_pay = 3*(remainder)
actualPay = pay+contract_pay
ultimatePAY=actualPay*(hoursWorked)
if kids == 14:
    print "Country Meadows --> $" + str(ultimatePAY) 
elif kids == 6:
    print "Hawthorne --> $" + str(ultimatePAY)
elif kids == 19:
    print "St. Mary --> $" + str(ultimatePAY)
else:
    print "$" + str(ultimatePAY)

    
