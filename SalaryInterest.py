import math
salary = 100
r = 10
i = 0
while i < 10:
    updatedSalary = salary*math.pow(1+r/100.0,i)
    i=i+1
print updatedSalary
