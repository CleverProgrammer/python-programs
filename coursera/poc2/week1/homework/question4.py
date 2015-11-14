"""
Question 4: Fibonacci Recurrence Relation
"""
counter = 0

def fib(num):
    global counter
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        counter += 1
        return fib(num - 1) + fib(num - 2)

if __name__ == '__main__': 
    num = int(input("Enter the nth term for the fibonacci sequence: "))
    print("fib result: ", fib(num))
    print("counter: ", counter)
    print("Theory: ", 2**num-1)
