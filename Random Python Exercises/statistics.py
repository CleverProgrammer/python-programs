# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 02:16:33 2015
Calculating the Median
@author: Rafeh
"""


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
        actual_median = mean([median1, median2])
        return actual_median
    else: 
        actual_median = x[(len(x)+1)//2]
        return actual_median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = median(donations)
    N = len(donations)
    print ('Mean donation over the last {0} days is {1}'.format(N, mean(donations)))
    print ('Median donation over the last {0} days is {1}'.format(N, median))

