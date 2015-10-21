"""
A simple testing suite for Solitaire Mancala
Note that tests are not exhaustive and should be supplemented
"""

import poc_simpletest

def run_suite(gen_all_holds):
    suite = poc_simpletest.TestSuite()
    
    # Check if you are holding only one dice with val 1.
    computed = gen_all_holds([1])
    expected = set([(), (1,)])
    suite.run_test(computed, expected, "test1")
    
    # Check if you are holding only two die with vals 1 and 4
    computed = gen_all_holds([1, 4])
    expected = set([(), (1,), (4,),(1,4)])
    suite.run_test(computed, expected, "test2")

    # Report the number of tests and failures
    suite.report_results()