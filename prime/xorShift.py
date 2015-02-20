import random
from os import urandom as _urandom
from binascii import hexlify as _hexlify


class Xorshift(random.Random):
    VERSION = (u'Xorshift', 1)

    def __init__(self, x=None):
        self._state = [1812433254, 3713160357, 3109174145, 64984499]
        self.seed(x)
        self.gauss_next = None

    def _genrand_int32(self):
        t = self._state[0] ^ ((self._state[0] << 11) & 0xffffffff)
        self._state[:] = self._state[1], self._state[2], self._state[3], \
                         (self._state[3] ^ (self._state[3] >> 19)) ^ (t ^ (t >> 8))
        return self._state[3]

    def random(self):
        a = self._genrand_int32() >> 5
        b = self._genrand_int32() >> 6
        return (a * 67108864.0 + b) * (1.0 / 9007199254740992.0)

    def seed(self, a=None):
        if a is None:
            try:
                a = int(_hexlify(_urandom(16)), 16)
            except NotImplementedError:
                import time

                a = long(time.time() * 256)
        elif isinstance(a, (int, long)):
            a = abs(a)
        else:
            a = hash(a) & 0xffffffff

        for i in range(1, 5):
            a = (1812433253 * (a ^ (a >> 30)) + i) & 0xffffffff
            self._state[i - 1] = a

        self.gauss_next = None

    def getstate(self):
        return self.VERSION, tuple(self._state), self.gauss_next

    def setstate(self, state):
        version = state[0]
        if version == (u'Xorshift', 1):
            self._state = list(state[1])
            self.gauss_next = state[2]
        else:
            raise ValueError()
