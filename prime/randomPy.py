from convert import *
import os


# generate random number from system random value

class RandomPy():
    def __init__(self):
        pass

    @staticmethod
    def read_random_bits(nbits):
        number_bytes, right_bits = divmod(nbits, 8)
        data = os.urandom(number_bytes)
        if right_bits > 0:
            rnd_value = ord(os.urandom(1))
            rnd_value >>= (8 - right_bits)
            data = byte(rnd_value) + data
        return data

    @staticmethod
    def read_random_int(nbits):
        data = RandomPy.read_random_bits(nbits)
        value = bytes2int(data)

        copy_value = value
        copy_value |= 1 << (nbits - 1)
        return copy_value

    '''
    @staticmethod
    def randint(minvalue, maxvalue):
        range = maxvalue - minvalue + 1
        return RandomPy.read_random_int(int2bytes(range)) + minvalue

    '''


def randint(minvalue, maxvalue):
    bsize = bit_size(maxvalue)
    tries = 0
    while True:
        value = RandomPy.read_random_int(bsize)
        if (value <= maxvalue) and (value >= minvalue):
            break

        if tries and tries % 10 == 0:
            bsize -= 1
        tries += 1
    return value