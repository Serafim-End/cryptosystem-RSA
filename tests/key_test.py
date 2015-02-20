import unittest
from math import pow
from key import GetKeys
import random


class KeyTests(unittest.TestCase):

    bits_array = [4, 8, 16, 32, 64, 128, 256]
    tests_numb = 100

    def setUp(self):
        self.min_key_bits = 4
        self.max_key_bits = 512
        self.success_tests = 0
        self.failed_test = 0

    def tearDown(self):
        pass

    def test_on_correct_key_pow_of_two(self):
        for bits in self.bits_array:
            for i in xrange(self.tests_numb):
                public_key, private_key = GetKeys.getKeys(bits)

                if pow(2, bits) > public_key['n'] > 0:
                    self.success_tests += 1

                else:
                    self.failed_test += 1

    def test_on_correct_key_not_pow_of_two(self):
        for test in xrange(self.tests_numb):
            public_key, private_key = GetKeys.getKeys(random.randint(self.min_key_bits, self.max_key_bits))
            if pow(2, test) > public_key['n'] > 0:
                self.success_tests += 1

            else:
                self.failed_test += 1

if __name__ == '__main__':
    unittest.main()