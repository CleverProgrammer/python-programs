def main():
    print ("This program is used to convert degrees in celsius to degrees in fahrenheit.")
    print ()
    print ()

    for i in range(5):
        
        celsius = input("Enter the degrees in celsius here: ")
        fahrenheit = (1.8*celsius)+32
        print (fahrenheit)

    print ("Celsius    Fahrenheit")
    for i in range(11):
        celsius = i * 10
        fahrenheit = (1.8*celsius)+32
        
        print (celsius, "          ", fahrenheit)
        

main()

