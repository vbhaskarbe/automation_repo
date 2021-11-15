#!/usr/bin/env python
#
# Example using `concurrencytest`:
#   https://github.com/cgoldberg/concurrencytest
 
import unittest
 
from concurrencytest import ConcurrentTestSuite, fork_for_tests
 
 
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
 
 
class FibonacciTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(31), 1346269)
 
 
if __name__ == '__main__':
 
    # load a TestSuite with 50x TestCases for demo
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for _ in range(50):
        suite.addTests(loader.loadTestsFromTestCase(FibonacciTestCase))
    print('Loaded %d test cases...' % suite.countTestCases())
 
    runner = unittest.TextTestRunner()
 
    print('\nRun tests sequentially:')
    runner.run(suite)
 
    print('\nRun same tests with 2 processes:')
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(2))
    runner.run(concurrent_suite)
 
    print('\nRun same tests with 4 processes:')
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(4))
    runner.run(concurrent_suite)
 
    print('\nRun same tests with 8 processes:')
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(8))
    runner.run(concurrent_suite)


