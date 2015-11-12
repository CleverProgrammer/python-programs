"""
Question 5: Memoization of Fibonacci Sequence
"""


counter = 0
def memoized_fib(num, memo_dict = {0: 0, 1:1}):
    global counter
    if num in memo_dict:
        return memo_dict[num]
    else:
        counter += 1
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

if __name__ == '__main__':
    num = int(input("Enter your number here: "))
    print("Fib result:", memoized_fib(num))
    print("Counter:", counter)
