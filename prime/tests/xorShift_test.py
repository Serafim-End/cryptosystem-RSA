import unittest
from math import pow
from time import clock
from prime.xorShift import Xorshift
from random import randint


class XorShiftTests(unittest.TestCase):

    test_number = 1000
    rnd_array = []

    def setUp(self):
        self.min_a = 1
        self.max_a = 100
        self.max_b = 1000

        self.seeds = [None] + [pow(2, i) for i in xrange(10)]

    def test_small_value(self):
        for i in xrange(self.test_number):
            for seed in self.seeds:

                xor = Xorshift(seed)

                a = randint(1, 100)
                b = randint(a, 1000)

                t1 = clock()
                result = xor.randint(a, b)
                t2 = clock()

                if result in self.rnd_array:
                    result = xor.randint(a, b)

                print "random number: ", result, "time: ", (t2-t1)*pow(10, 6)
                self.rnd_array.append(result)
                self.assertIsInstance(result, (int, long))
                self.assertTrue((result >= a) and (result <= b))

if __name__ == '__main__':
    unittest.main()
