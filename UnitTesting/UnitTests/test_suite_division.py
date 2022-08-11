import unittest

from test_math_operations import TestDivision


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestDivision))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


my_suite()