from eea import *
from random import randint, random
from convert import int2str64
import unittest


class GcdTests(unittest.TestCase):
    def setUp(self):
        self.testsNumb = 100
        self.success_tests = None

    def test_in_correct_numbers(self):
        self.success_tests = 0
        for i in xrange(self.testsNumb):
            a, b = randint(1, 10000), randint(1, 10000)
            result = egcd(a,  b)[2]
            self.assertTrue(result == gcd(a, b))
            self.success_tests += 1
        print "gcd correct numbers success tests: ", self.success_tests

    def test_in_incorrect_numbers(self):
        self.success_tests = 0
        for i in xrange(self.testsNumb):
            a, b = randint(1, 10000) + random(), randint(1, 10000) + random()
            result = egcd(int(a), int(b))[2]
            self.assertTrue(result == gcd(a, b))
            self.success_tests += 1
        print "gcd incorrect numbers success tests: ", self.success_tests

    def test_in_except_values(self):
        self.success_tests = 0
        for i in xrange(self.testsNumb):
            a, b = int2str64(randint(100, 10000)), int2str64(randint(100, 10000))
            result = "Incorrect data"
            self.assertTrue(result == gcd(a, b))
            self.success_tests += 1
        print "gcd except values success tests: ", self.success_tests


class EgcdTests(unittest.TestCase):
    def setUp(self):
        self.testsNumb = 100
        self.success_tests = None

    def test_in_correct_numbers(self):
        self.success_tests = 0
        for i in xrange(self.testsNumb):
            a, b = randint(1, 10000), randint(1, 10000)
            result = gcd(a, b)
            self.assertTrue(result == egcd(a, b)[2])
            self.success_tests += 1
        print "egcd correct numbers success tests: ", self.success_tests

    def test_in_incorrect_numbers(self):
        self.success_tests = 0
        for i in xrange(self.testsNumb):
            a, b = randint(1, 10000) + random(), randint(1, 10000) + random()
            result = gcd(int(a), int(b))
            self.assertTrue(result == egcd(a, b)[2])
            self.success_tests += 1
        print "egcd incorrect values success tests: ", self.success_tests

    def test_in_except_values(self):
        self.success_tests = 0
        for i in xrange(self.testsNumb):
            a, b = int2str64(randint(100, 10000)), int2str64(randint(100, 10000))
            result = "Incorrect data"
            self.assertTrue(result == egcd(a, b))
            self.success_tests += 1
        print "egcd except values success tests: ", self.success_tests

if __name__ == '__main__':
    unittest.main()