from randnum import Random
from randomPy import *


class Prime():
    def __init__(self):
        pass

    # try to solve problems with bits (not bytes)

    @staticmethod
    def randint_my_random(minvalue, maxvalue):
        rang = maxvalue - minvalue + 1
        rnd = Random()
        return rnd.getrandbits(int(math.log(rang, 2))) + minvalue

    @staticmethod
    def jacobi(a, b):
        # Calculates the value of the Jacobi symbol (a/b)
        # where both a and b are positive integers, and b is odd

        if a == 0:
            return 0
        result = 1
        while a > 1:
            if a & 1:
                if ((a - 1) * (b - 1) >> 2) & 1:
                    result = -result
                a, b = b % a, a
            else:
                if (((b * b) - 1) >> 3) & 1:
                    result = -result
                a >>= 1
        if a == 0:
            return 0
        return result

    def witness(self, x, n):
        j = self.jacobi(x, n) % n
        f = pow(x, (n - 1) / 2, n)
        if j == f:
            return False
        return True

    def randomized_primality_testing(self, n, k):
        for i in xrange(k):
            # x = self.randintMyRandom(1, n-1)
            # x = Prime.randintMyRandom(1, n - 1)

            x = randint(1, n - 1)
            if self.witness(x, n):
                return False
        return True

    def is_prime(self, number):
        if self.randomized_primality_testing(number, 6):
            return True
        return False

    @staticmethod
    def getprime(self, nbits):
        while True:
            integer = RandomPy.read_random_int(nbits)
            integer |= 1
            if self.is_prime(integer):
                break
        return integer