import math
import types
from struct import pack


# Converts a number between 0 and 255 (both inclusive) to a base-256 (byte)
def byte(num):
    return pack("B", num)


def bit_size(number):
    return int(math.ceil(math.log(number, 2)))


def bits2int(bits):
    integer = 0
    for bit in bits:
        integer *= 2
        bit = ord(bit)
        integer += bit
    return integer


def bytes2int(bytes_):
    if not (isinstance(bytes, types.ListType) or isinstance(bytes_, types.StringType)):
        raise TypeError("You must pass a string or a list")
    integer = 0
    for byte_ in bytes_:
        integer *= 256
        if isinstance(byte_, types.StringType):
            byte_ = ord(byte_)
        integer += byte_
    return integer


def int2bytes(number):
    if not (isinstance(number, types.LongType) or isinstance(number, types.IntType)):
        raise TypeError("You must pass a long or an int")
    string = ""
    while number > 0:
        string = "%s%s" % (byte(number & 0xFF), string)
        number /= 256
    return string


def to64(number):
    if not (isinstance(number, types.LongType) or isinstance(number, types.IntType)):
        raise TypeError("You must pass a long or an int")

    if 0 <= number <= 9:  # 00-09 translates to '0' - '9'
        return byte(number + 48)

    if 10 <= number <= 35:
        return byte(number + 55)  # 10-35 translates to 'A' - 'Z'

    if 36 <= number <= 61:
        return byte(number + 61)  # 36-61 translates to 'a' - 'z'

    if number == 62:  # 62   translates to '-' (minus)
        return byte(45)

    if number == 63:  # 63   translates to '_' (underscore)
        return byte(95)

    raise ValueError('Invalid Base64 value: %i' % number)


def from64(number):
    if not (isinstance(number, types.LongType) or isinstance(number, types.IntType)):
        raise TypeError("You must pass a long or an int")

    if 48 <= number <= 57:  # ord('0') - ord('9') translates to 0-9
        return number - 48

    if 65 <= number <= 90:  # ord('A') - ord('Z') translates to 10-35
        return number - 55

    if 97 <= number <= 122:  # ord('a') - ord('z') translates to 36-61
        return number - 61

    if number == 45:  # ord('-') translates to 62
        return 62

    if number == 95:  # ord('_') translates to 63
        return 63

    raise ValueError('Invalid Base64 value: %i' % number)


def int2str64(number):
    if not (isinstance(number, types.LongType) or isinstance(number, types.IntType)):
        raise TypeError("You must pass a long or an int")
    string = ""
    while number > 0:
        string = "%s%s" % (to64(number & 0x3F), string)
        number /= 64

    return string


def str642int(string):
    if not (isinstance(string, types.ListType) or isinstance(string, types.StringType)):
        raise TypeError("You must pass a string or a list")
    integer = 0
    for byte_ in string:
        integer *= 64
        if isinstance(byte_, types.StringType):
            byte_ = ord(byte_)
        integer += from64(byte_)
    return integer


# bytes and bits converts

def bit_size(num):
    if num == 0:
        return 0
    if num < 0:
        num = -num

    # Make sure this is an int and not a float.
    # num & 1

    hex_num = "%x" % num
    return ((len(hex_num) - 1) * 4) + {
        '0': 0, '1': 1, '2': 2, '3': 2,
        '4': 3, '5': 3, '6': 3, '7': 3,
        '8': 4, '9': 4, 'a': 4, 'b': 4,
        'c': 4, 'd': 4, 'e': 4, 'f': 4,
    }[hex_num[0]]


def _bit_size(number):
    if number < 0:
        raise ValueError('Only nonnegative numbers possible: %s' % number)
    if number == 0:
        return 0

    bits = 0
    while number:
        bits += 1
        number >>= 1
    return bits


def byte_size(number):
    quanta, mod = divmod(bit_size(number), 8)
    if mod or number == 0:
        quanta += 1
    return quanta