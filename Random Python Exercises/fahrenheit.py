def main():
    print ("This program is used to convert degrees in Fahrenheit to degrees in Celsius.")
    print ()
    print ()

    for i in range(5):
        
        fahrenheit = input("Enter the degrees in fahrenheit here: ")
        celsius = (fahrenheit/1.8)-(32/1.8)
        print (celsius)
main()
