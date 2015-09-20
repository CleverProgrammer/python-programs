def expected_value(range_start,range_end, total_outcomes):
    sample_space = sum(range(range_start, range_end+1)) 
    #arithmetic_sum_formula = .5*(sample_space)*(sample_space+1)
    return sample_space * (1.0/total_outcomes)
