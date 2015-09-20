def expected_value(range_start,range_end, total_outcomes):
    sample_space = sum(range(range_start, range_end+1)) 
    list_of_tuples = [] 
    for first in range(range_start, range_end+1):
     for second in range(range_start, range_end+1):
      list_of_tuples.append( (first, second) )
    sums = [sum(tuple) for tuple in list_of_tuples]
    #counts = [sums.count(i) for i in range(range_start, range_end+1)]
    counts = []
    for i in range(sums[0], sums[-1]):
     counts.append(sums.count(i))
     
    print("list_of_tuples: %s" %list_of_tuples)
    print("sums: %s" %sums)
    print("counts: %s" %counts)
    #arithmetic_sum_formula = .5*(sample_space)*(sample_space+1)
    return sample_space * (1.0/total_outcomes)
