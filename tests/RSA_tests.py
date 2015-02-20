from RSA import Crypt
from key import GetKeys
from convert import int2str64
from random import randint

import unittest


class RSATests(unittest.TestCase):
    def setUp(self):
        self.bits_numb = [32, 64, 128, 256, 512, 1024, 2048, 4096]
        self.min_text_simbols = 10
        self.max_text_simbols = 1000000
        self.tests_numb = 1
        self.tests_success = None

    def tearDown(self):
        print "tests success", self.tests_success

    def test_in_correct_numbers(self):
        self.tests_success = 0
        for bits in self.bits_numb:
            for i in xrange(self.tests_numb):

                print "test number: ", i, " on different bits: ", bits
                public, private = GetKeys.getKeys(bits)

                message = int2str64(randint(self.min_text_simbols*64, self.max_text_simbols*64))
                print "message: ", message

                encrypted = Crypt.encrypt(message, public)
                decrypted = Crypt.decrypt(encrypted, private)

                self.assertTrue(message == decrypted)

                self.tests_success += 1
                print

    def test_in_big_message(self):

        self.tests_success = 0
        bits = self.bits_numb[3]

        min_long_text = 64 * 1000000
        max_long_text = 64 * 1000000000

        for i in xrange(self.tests_numb):
            print "test number", i, " on long message"
            public, private = GetKeys.getKeys(bits)

            message = int2str64(randint(min_long_text, max_long_text))
            print "message: ", message

            encrypted = Crypt.encrypt(message, public)
            decrypted = Crypt.decrypt(encrypted, private)

            self.assertTrue(message == decrypted)

            self.tests_success += 1

            print