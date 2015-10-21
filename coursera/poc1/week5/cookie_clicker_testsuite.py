import poc_simpletest


def run_suite(game_class):
    suite = poc_simpletest.TestSuite()

    # get_cps(): first cps should be 1
    obj1 = game_class()
    computed = obj1.get_cps()
    expected = 1
    suite.run_test(computed, expected, "test1 get_cps")

    # time_until(): 10 seconds for 10 cookies with 1 cps as start
    obj1 = game_class()
    computed = obj1.time_until(10)
    expected = 10
    suite.run_test(computed, expected, "test2 time_until")

    # buy_item(self, item_name, cost, additional_cps)
    obj1 = game_class()
    obj1.buy_item('Grandma', 100, 0.6)
    computed = obj1.get_cps()
    expected = 1.6
    suite.run_test(computed, expected, "test3 buy_item")

    suite.report_results()
