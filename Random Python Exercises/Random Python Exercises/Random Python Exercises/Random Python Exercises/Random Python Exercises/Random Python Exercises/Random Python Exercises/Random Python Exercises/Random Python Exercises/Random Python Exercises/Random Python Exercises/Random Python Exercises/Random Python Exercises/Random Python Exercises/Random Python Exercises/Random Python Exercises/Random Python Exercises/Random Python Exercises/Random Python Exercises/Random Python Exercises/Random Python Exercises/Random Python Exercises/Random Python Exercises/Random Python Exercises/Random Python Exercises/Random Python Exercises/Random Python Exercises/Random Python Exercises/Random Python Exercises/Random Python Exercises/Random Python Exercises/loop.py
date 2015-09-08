import math
def f(x):
    q = 150./((x+1.)*(x+1.))
    return q

n = 0
for i in range(0,6):
    f(n)
    n=n+1
    print f(n)

    
    
