'''
6 sided die simulation
'''

def die():
    from random import randint as r
    x = []
    for i in range(50):
        die = r(1,6)
        x.append(die)
    print (x)
    return x

if __name__ == '__main__':
    die()

    
        
