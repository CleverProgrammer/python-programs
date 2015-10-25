counter = 0

def fib(num):
    global counter
    counter += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

if __name__ == '__main__': 
    num = int(input("Enter the nth term for the fibonacci sequence: "))
    print("fib result: ", fib(num))
    print("counter: ", counter)
