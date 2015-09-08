'''
Even-Odd Vending Machine, which will take a number as input
and do two things:
1. Print whether the number is even or odd.
2. Display the number followed by the next 9 even or odd numbers.
'''

def even(number):
    print ('{0} is an even number'.format(number))
    for i in range (number, number + 18, 2):
        print (i)

def odd(number):
    print ('{0} is an odd number'.format(number))
    for i in range (number, number + 18, 2):
        print (i)

if __name__ == '__main__':
    number = int(input('Enter your number here: '))
    
    if number % 2 == 0:
        even(number)
    else:
        odd(number)


        
        
        
