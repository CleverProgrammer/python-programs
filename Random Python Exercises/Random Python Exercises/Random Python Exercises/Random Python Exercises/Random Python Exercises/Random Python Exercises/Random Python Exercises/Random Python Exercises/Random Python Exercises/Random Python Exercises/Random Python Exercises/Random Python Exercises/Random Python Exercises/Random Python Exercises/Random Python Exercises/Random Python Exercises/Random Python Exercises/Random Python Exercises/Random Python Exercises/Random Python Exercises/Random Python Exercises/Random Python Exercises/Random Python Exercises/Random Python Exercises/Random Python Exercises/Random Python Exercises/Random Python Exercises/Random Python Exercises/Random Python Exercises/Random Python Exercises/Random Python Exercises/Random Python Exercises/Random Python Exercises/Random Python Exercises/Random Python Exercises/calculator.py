def main():
    print ("This program allows the use python as a calculator")
    print()
    print()

    for i in range(100):
        calculation = eval(input("Enter an expression: "))
        print (calculation)

main()
