def main ():
    print ("This program calculates the future value")
    print ("of a given-year investment.")
    print ()
    print ()

    years = eval(input("Enter the number of years of investment: "))
    principal = eval(input("Enter the initial principal: "))
    investment = eval(input("Enter the investment per year: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(years):
        if i == 0:
            principal = principal * (1+apr)
        else:
            principal = (principal*(1+apr))+investment

        print ("The value in", i+1, "years is:", principal)

main()
