import time
from random import randint
from arithmetika.multiplication import *


class Tests_polymult():
    def __init__(self, arg, number_of_tests, power_of_test_start, power_of_test_end):
        self.n = number_of_tests
        self.start = power_of_test_start
        self.end = power_of_test_end
        if arg == 'computer_test':
            self.computer_test()
        if arg == 'handle_test':
            self.handle_test()

    def test(self):
        for i in xrange(self.n):
            rand_1, rand_2 = randint(10 ** self.start, 10 ** self.end), randint(10 ** self.start, 10 ** self.end)
            rand_1_ar, rand_2_ar = scaleofnotation(rand_1), scaleofnotation(rand_2)
            t3 = time.clock()
            python_mult = rand_1 * rand_2
            t4 = time.clock()
            t1 = time.clock()
            mult = polymult(rand_1_ar, rand_2_ar)
            t2 = time.clock()

            if str(python_mult) == str(int(backscaleofnotation(mult))):
                print i, '| ', rand_1, '*', rand_2, ' |', True, \
                    '|shebhage ', t2 - t1, '|py ', t4 - t3, '|shenhage - py ', (t4 - t3) - (t2 - t1)
            else:
                print i, '| ', rand_1, '*', rand_2, ' |', False
        return

    @staticmethod
    def handle_test():
        try:
            a, b = input('a: '), input('b: ')
            a_ar, b_ar = scaleofnotation(a), scaleofnotation(b)
            mult_fft = polymult(a_ar, b_ar)
            mult_python = a * b
            if int(backscaleofnotation(mult_fft)) == mult_python:
                print True
            else:
                print "fft real - it is not all in this situation : result is not correct!"
            print 'difference in multiplication: ', mult_fft - mult_python
        except ValueError:
            print "Not today!"

    def computer_test(self):
        try:
            self.test()
            return
        except ValueError:
            print "Not today!"


class TestsPolymultInt():
    def __init__(self, arg, number_of_tests, power_of_test_start, power_of_test_end):
        self.n = number_of_tests
        self.start = power_of_test_start
        self.end = power_of_test_end
        if arg == 'computer_test':
            self.computer_test()
        if arg == 'handle_test':
            self.handle_test()

    def test(self):
        for i in xrange(self.n):
            rand_1, rand_2 = randint(10 ** self.start, 10 ** self.end), randint(10 ** self.start, 10 ** self.end)
            rand_1_ar, rand_2_ar = scaleofnotation(rand_1), scaleofnotation(rand_2)
            t3 = time.clock()
            python_mult = rand_1 * rand_2
            t4 = time.clock()
            t1 = time.clock()
            mult = polymult_int(rand_1_ar, rand_2_ar)
            t2 = time.clock()
            if str(python_mult) == str(mult):
                print i, '| ', rand_1, '*', rand_2, ' |', True, \
                    '|shebhage ', t2 - t1, '|py ', t4 - t3, '|shenhage - py ', (t4 - t3) - (t2 - t1)
            else:
                print i, '| ', rand_1, '*', rand_2, ' |', False
        return

    @staticmethod
    def handle_test():
        try:
            a, b = input('a: '), input('b: ')
            a_ar, b_ar = scaleofnotation(a), scaleofnotation(b)
            mult_fft = polymult_int(a_ar, b_ar)
            mult_python = a * b

            if mult_fft == mult_python:
                print True
            else:
                print "fft real - it is not all in this situation : result is not correct!"
            print 'difference in multiplication: ', mult_fft - mult_python
        except ValueError:
            print "Not today!"

    def computer_test(self):
        try:
            self.test()
            return
        except ValueError:
            print "Not today!"


class PolymultSourceLength:
    def __init__(self):
        pass

    @staticmethod
    def main():
        a = scaleofnotation(11)
        print 'a: ', a
        b = scaleofnotation(11)
        print 'b: ', b
        mult = polymult_source_length(a, b, False)
        print 'mult: ', int(backscaleofnotation(mult))
        print 'mult bin: ', mult


def poly():
    try:
        for i in xrange(300, 400, 10):
            TestsPolymultInt('computer_test', 5, i - 3, i)
    except ValueError:
        print "Some problem with int multiplication!"
    try:
        # multiplication at all
        for i in xrange(300, 400, 10):
            Tests_polymult('computer_test', 5, i - 3, i)
    except ValueError:
        print "Some problem with notation scale!"
    return


if __name__ == "__main__":
    poly()