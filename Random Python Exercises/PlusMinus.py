# Enter your code here. Read input from STDIN. Print output to STDOUT

# positive_tracker = +1 if number > 0
# negative_tracker = +1 if number < 0
# zero_tracker     =  0 if number == 0
# give fraction of each kind of number

from __future__ import division
from sys import STDIN

#s1 = STDIN.readline() # Read user input
s1 = input()
positive_tracker = 0
negative_tracker = 0
zero_tracker = 0

s2 = map(int,raw_input().split()) # accept input as string. Create a list of numbers removing the empty strings (spaces). 
								  # map each string as an integer

for i in s2:
    if i > 0:
        positive_tracker += 1
    if i < 0:
        negative_tracker += 1
    if i == 0:
    	zero_tracker += 1

p = positive_tracker / s1
n = negative_tracker / s1
z = zero_tracker / s1

print(" %0.3f " % p)
print(" %0.3f " % n)
print(" %0.3f " % z)