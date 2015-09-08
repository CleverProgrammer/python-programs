# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 02:16:33 2015
Calculating the Median
@author: Rafeh
"""

from collections import Counter

def mean(x):
    return sum(x)/len(x)
    
def median(x):
    x.sort()
    
    if len(x) % 2 == 0: 
        # if length of list is even
        mid_of_list = len(x)//2
        one_more_than_mid = (len(x)//2)+1
        median1 = x[mid_of_list - 1] 
        median2 = x[one_more_than_mid - 1]
        #Subtract 1 because index starts at 0 and NOT 1
        print ('median1', median1)
        print ('median2', median2)
        actual_median = mean([median1, median2]) # because mean function takes lists only
        return actual_median
        
    else: 
        actual_median = x[(len(x)+1)//2]
        return actual_median
        
def mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    # returns a list of tuples (number, frequency) in descending order
    max_count = numbers_freq[0][1]
    #Accessing the frequency of the first tuple (The one with the greatest frequency)
    
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            #if the 2nd element of the tuple in numbers_freq is == max_count, 
            #Second element being the frequency

            modes.append(num[0])
            #Basically iterates through frequencies appending to modes list only the numbers
            #With the highest frequency.
            
    return modes
    
'''
6 sided die simulation
'''



if __name__ == '__main__':
    from random import randint as r
    die_list = []
    for i in range(50):
        die_result = r(1,6)
        die_list.append(die_result)
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    #median = median(donations)
    median_die = median(die_list)
    modes = mode(donations)
    N = len(donations)
    print ('Mean donation over the last {0} days is {1}'.format(N, mean(donations)))
   # print ('Median donation over the last {0} days is {1}'.format(N, median))
    print ('Mode donation over the last {0} days is {1}'.format(N, modes))
    print ('The mode(s) for the list of numbers are: ')
    print ('Die simulation mode: {0}'.format(mode(die_list)))
    print ('Die simulation mean: {0}'.format(mean(die_list)))
    print ('Die simulation median: {0}'.format(median_die))
    print (die_list)
