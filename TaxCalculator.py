pay = input("Enter income before tax:")
taxedPay = input ("Enter income after tax:")
remainder = pay-taxedPay+0.0
tax = (remainder/pay)*100.0
decimalTax = "%0.2f" % tax
print "You are taxed " + str (decimalTax) + "%."

