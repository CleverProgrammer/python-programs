def main():
    print ("This program illustrates a chaotic function")
    n = eval(input("How many numbers of values should I put?"))
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a second number between 0 and 1: "))
    print (str(x),str(y))
    print ("---- ----")
    for i in range(n):
	    x = 3.9*x*(1-x)
	    y = 3.9*x*(1-x)
	    print (str(x),str(y))

main ()
