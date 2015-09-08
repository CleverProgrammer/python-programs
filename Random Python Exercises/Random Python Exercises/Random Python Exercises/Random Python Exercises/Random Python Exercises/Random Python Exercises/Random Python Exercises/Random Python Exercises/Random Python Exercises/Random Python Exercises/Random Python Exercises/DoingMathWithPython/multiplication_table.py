'''
Multiplication Table
'''

def multiplication_table(a, n):
    for i in range (1, n+1):
        b = a * i
        print ('{0} * {1} = {2}'.format(a,i,b))



if __name__ == '__main__':

    choice = 0
    while True:

        a = float(input('Enter your positive integer here: '))
        n = int(input('Mulitplication depth desired: '))

        if a > 0 and a.is_integer():
            multiplication_table(a, n)
        else:
            print ('Enter a positive integer idiot')
        answer = input('Do you want to exit? (Y) for yes: ')
        if answer == 'y':
            break
