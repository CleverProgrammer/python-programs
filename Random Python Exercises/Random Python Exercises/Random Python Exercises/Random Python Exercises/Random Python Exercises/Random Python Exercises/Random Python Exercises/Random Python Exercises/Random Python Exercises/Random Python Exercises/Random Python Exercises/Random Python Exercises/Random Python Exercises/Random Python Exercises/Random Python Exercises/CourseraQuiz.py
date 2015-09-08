count = 0

def square(x):
    global count
    count += 1
    return x**2

print square(square(square(square(3))))
print count
