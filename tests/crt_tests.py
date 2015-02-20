import unittest
from random import randint
from crt import crt


class CrtTests(unittest.TestCase):
    def setUp(self):
        self.testsNumb = 100

    def test_correct_numbers_known_results(self):
        first = [[2, 3, 2], [2, 3], [2, 3, 0]]
        second = [[3, 5, 7], [3, 5], [7, 11, 15]]
        known_results = [23, 8, 135]
        for i in xrange(3):
            self.assertTrue(known_results[i] == crt(first[i], second[i]))

    def test_unknown_results(self):
        for j in xrange(self.testsNumb):
            rang = randint(2, 65)
            first = [randint(1, 100000) for i in xrange(rang)]
            second = [randint(1, 100000) for i in xrange(rang)]
            result = crt(first, second)
            print "unknown results ", j, " : ", result
            self.assertIsInstance(result, (int, long))

if __name__ == '__main__':
    unittest.main()