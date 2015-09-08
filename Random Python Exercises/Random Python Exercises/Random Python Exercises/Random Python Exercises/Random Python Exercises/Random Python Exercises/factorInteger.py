'''
Find all the factors of a given integer
'''

def factor(a):


    for i in range (1,a+1):
        if a % i == 0:
            print (i)

if __name__ == '__main__':


    a = float(input('Enter your integer here: '))

    if a > 0 and a.is_integer():
        factor(int(a))
    else:
        print ('Please enter a positive integer')
