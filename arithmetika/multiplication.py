from math import log, ceil
from cmath import exp, pi
from notationScales import equal
from notationScales import backscaleofnotation
from sum import *


# fff and ifft
def fft(binary_array, back):
    n = len(binary_array)
    if n <= 1:
        return binary_array
    else:
        even_array = [binary_array[i] for i in xrange(0, len(binary_array), 2)]
        odd_array = [binary_array[i] for i in xrange(1, len(binary_array), 2)]
        even, odd = fft(even_array, back), fft(odd_array, back)
        if back:
            return [even[k] + exp(-2j * pi * k / n) * odd[k] for k in xrange(n / 2)] + \
                   [even[k] - exp(-2j * pi * k / n) * odd[k] for k in xrange(n / 2)]
        else:
            return [(even[k] + exp(2j * pi * k / n) * odd[k]) / 2 for k in xrange(n / 2)] + \
                   [(even[k] - exp(2j * pi * k / n) * odd[k]) / 2 for k in xrange(n / 2)]


# polynomial multiplication

def polymult(a, b=None, inverse=False):  # polynomial multiplication
    # a -- array with the coefficients of the first polynomial
    # b -- array with the coefficients of the second polynomial (default: None)
    # Determine n, the minimum index for the DFT. (FFT because recurs)

    n = (len(a) + len(b) - 1) if b else (2 * len(a) - 1)  # max length of number in multiplication length(a)+length(b)-1
    n = int(ceil(log(n, 2)))  # Round up to next power of 2.

    a = equal(a, n)  # len(a) must be power of 2
    b = equal(b, n) if b else a  # in this situation len(a) = len(b)

    if inverse:
        a, b = a[::-1], b[::-1]  # invert arrays | arrays must be power of 2

    d_a = fft(a, True)  # d_a = DFT(a)
    d_b = fft(b, True) if b else d_a  # d_b = DFT(b)

    d = [d_a[i] * d_b[i] for i in xrange(len(a))]  # DFT(a)*DFT(b)

    ifft_ar = fft(d, False)  # inverseFFT = a*b = InverseDFT(DFT(a)*DFT(b))

    real = [int(i.real + 0.5) for i in ifft_ar]  # only real part of complex is not correct if number is long
    return real  # real numbers notation scale 10


def polymult_int(a, b=None, inverse=False):  # polynomial multiplication
    return int(backscaleofnotation(polymult(a, b, inverse)))  # real numbers notation scale


def polynomial_binary_decorator(function):
    def wrapped(*args):
        polynomialMultiplication = function(*args)
        for i in xrange(len(polynomialMultiplication)):
            if polynomialMultiplication[i] > 1:
                polynomialMultiplication[i] %= 2
                polynomialMultiplication[i + 1] += 1
        i = len(polynomialMultiplication) - 1
        while i != 1: i -= 1
        return polynomialMultiplication[:len(polynomialMultiplication) - i:]

    return wrapped


@polynomial_binary_decorator
def polymult_source_length(a, b=None, inverse=False):
    return polymult(a, b, inverse)


def main():
    a = scaleofnotation(12309483)
    print 'a: ', a
    b = scaleofnotation(12734623)
    print 'b: ', b
    mult = polymult_source_length(a, b, False)
    print 'mult: ', int(backscaleofnotation(mult))
    print 'mult bin: ', mult
    print len(mult)


if __name__ == '__main__':
    main()
