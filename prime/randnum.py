from warnings import warn as _warn
from types import MethodType as _MethodType, BuiltinMethodType as _BuiltinMethodType
import _random
from math import log, exp, pi, sqrt

# constants
# python random
NV_MAGICCONST = 4 * exp(-0.5)/sqrt(2.0)
TWOPI = 2.0*pi
LOG4 = log(4.0)
SG_MAGICCONST = 1.0 + log(4.5)
BPF = 53                                                               # Number of bits in a float
RECIP_BPF = 2**-BPF


class Random(_random.Random):
    def __init__(self):
        pass

    def randrange(self, start, stop=None, step=1, _int=int, maxwidth=1L << BPF):
        istart = _int(start)
        if istart != start:
            raise Exception(ValueError), "non-integer arg 1 for randrange()"
        if stop is None:
            if istart > 0:
                if istart >= maxwidth:
                    return self._randbelow(istart)
                return _int(self.random() * istart)
            raise Exception(ValueError), "empty range for randrange()"

        # stop argument supplied.
        istop = _int(stop)
        if istop != stop:
            raise Exception(ValueError), "non-integer stop for randrange()"
        width = istop - istart

        if step == 1 and width > 0:
            if width >= maxwidth:
                return _int(istart + self._randbelow(width))
            return _int(istart + _int(self.random()*width))
        if step == 1:
            raise Exception(ValueError), \
                "empty range for randrange() (%d,%d, %d)" % (istart, istop, width)

        # Non-unit step argument supplied.
        istep = _int(step)
        if istep != step:
            raise Exception(ValueError), "non-integer step for randrange()"
        if istep > 0:
            n = (width + istep - 1) // istep
        elif istep < 0:
            n = (width + istep + 1) // istep
        else:
            raise Exception(ValueError), "zero step for randrange()"

        if n <= 0:
            raise Exception(ValueError), "empty range for randrange()"

        if n >= maxwidth:
            return istart + istep*self._randbelow(n)
        return istart + istep*_int(self.random() * n)

    def randint(self, a, b):
        """Return random integer in range [a, b], including both end points.
        """

        return self.randrange(a, b+1)

    def _randbelow(self, n, log = log, _int=int, _maxwidth=1L << BPF,
                   _Method = _MethodType, _BuiltinMethod = _BuiltinMethodType):

        try:
            getrandbits = self.getrandbits
        except AttributeError:
            pass
        else:
            # Only call self.getrandbits if the original random() builtin method
            # has not been overridden or if a new getrandbits() was supplied.
            # This assures that the two methods correspond.
            if type(self.random) is _BuiltinMethod or type(getrandbits) is _Method:
                k = _int(1.00001 + log(n-1, 2.0))   # 2**k > n-1 > 2**(k-2)
                r = getrandbits(k)
                while r >= n:
                    r = getrandbits(k)
                return r
        if n >= _maxwidth:
            _warn("Underlying random() generator does not supply \n"
                "enough bits to choose from a population range this large")
        return _int(self.random() * n)

if __name__ == '__main__':
    rnd = Random()
    print rnd.randrange(1, 100)