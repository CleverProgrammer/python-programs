donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]

def mean(x):
    return sum(x)/len(x)

print ('Mean donation over the last {0} days is {1}'.format(len(donations), mean(donations)))

def median(x):
    x.sort()
    if len(x) % 2 == 0: 
        median1 = x[len(x)//2] 
        median2 = x[(len(x)//2)+1]
        actual_median = mean([median1, median2])
        return actual_median
    else: 
        actual_median = x[(len(x)+1)//2]
        return actual_median

print ('Median donation over the last {0} days is {1}'.format(len(donations), median(donations)))
