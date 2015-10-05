import unittest
import tests

suite = unittest.TestLoader().loadTestsFromTestCase(tests.Yahtzee)
unittest.TextTestRunner(verbosity=2).run(suite)
