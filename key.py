from prime.prime import Prime
from arithmetika.multiplication import polymult_int
from arithmetika.notationScales import *
from eea import *


class Key():
    def __init__(self):
        self.prime = Prime()

    @staticmethod
    def are_relatively_prime(a, b):
        d = gcd(a, b)
        return d == 1

    def find_p_q(self, nbits):
        pbits = nbits + (nbits / 16)  # Make sure that p and q aren't too close
        qbits = nbits - (nbits / 16)  # or the factoring programs can factor n
        p = Prime.getprime(self.prime, pbits)
        while True:
            q = Prime.getprime(self.prime, qbits)
            if not q == p:
                break
        return p, q

    def calculate_keys(self, p, q, nbits):
        n = polymult_int(scaleofnotation(p), scaleofnotation(q))
        phi_n = polymult_int(scaleofnotation(p - 1), scaleofnotation(q - 1))

        while True:
            # Make sure e has enough bits so we ensure "wrapping" through
            # modulo n
            # e = max(65537,Prime.getprime(self.prime, nbits/4))
            e = Prime.getprime(self.prime, nbits / 4)
            if Key.are_relatively_prime(e, n) and Key.are_relatively_prime(e, phi_n):
                break

        (i, j, d) = egcd(e, phi_n)

        if not d == 1:
            raise Exception("e (%d) and phi_n (%d) are not relatively prime" % (e, phi_n))
        if i < 0:
            raise Exception("New extended_gcd shouldn't return negative values")
        if not (e * i) % phi_n == 1:
            raise Exception("e (%d) and i (%d) are not mult. inv. modulo phi_n (%d)" % (e, i, phi_n))

        return e, i

    def gen_keys(self, nbits):
        (p, q) = self.find_p_q(nbits)
        (e, d) = self.calculate_keys(p, q, nbits)

        return p, q, e, d

    def newkeys(self, nbits):
        nbits = max(4, nbits)  # Don't let nbits go below 4 bits
        (p, q, e, d) = self.gen_keys(nbits)
        print "p: ", p
        print "q: ", q
        return {'e': e, 'n': p * q}, {'d': d, 'p': p, 'q': q}


class GetKeys:
    def __init__(self):
        pass

    @staticmethod
    def get_keys(bits_numb):
        key = Key()
        return key.newkeys(bits_numb)