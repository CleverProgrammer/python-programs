    # initialize necessary local variables
    clicker_state.current_seconds = 0
    current_salary = INITIAL_SALARY
    total_salary = 0
    current_bribe_cost = INITIAL_BRIBE_COST
    current_money = 0
    days_till_next_bribe = 0
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while clicker_state.current_seconds <= days_in_simulation:
        days_till_next_bribe = math.ceil((current_bribe_cost - current_money) / current_salary)
        clicker_state.current_seconds += days_till_next_bribe
        current_money += current_salary * days_till_next_bribe
        total_salary += current_salary * days_till_next_bribe
        # check whether we have enough savings to bribe without waiting
        while current_money >= current_bribe_cost:
            if clicker_state.current_seconds > days_in_simulation:
                return days_vs_earnings
            current_money -= current_bribe_cost
            if plot_type == STANDARD:
                days_vs_earnings.append((clicker_state.current_seconds, total_salary))
            else:
                days_vs_earnings.append([math.log(clicker_state.current_seconds), math.log(total_salary)])
            current_salary += SALARY_INCREMENT
            current_bribe_cost += bribe_cost_increment
