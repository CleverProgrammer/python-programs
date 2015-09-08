def main():
    print ("Change Counter")
    print ()
    print ("Please enter the count of each coin type.")
    quarters = eval(input("Enter the number of quarters here: "))
    dime = eval(input("Enter the number of dime here: "))
    nickel = eval(input("Enter the number of nickel here: "))
    cent = eval(input("Enter the number of cent here: "))
    print (quarters*0.25 + dime * 0.10 + nickel * 0.05 + cent * 0.01)

main ()
