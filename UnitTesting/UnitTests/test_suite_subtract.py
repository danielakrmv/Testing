import unittest

from test_math_operations import TestSubtract


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestSubtract))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


my_suite()