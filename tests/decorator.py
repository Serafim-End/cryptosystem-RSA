from time import clock

from arithmetika.multiplication import polymult_int
from arithmetika.notationScales import scaleofnotation


def scale_transform(function):
    def wrapped(*args):
        array = []
        for arg in args:
            array.append(function(arg))
        return array
    return wrapped


def times(function):
    def wrapped(*args):
        mult = 1
        time_1 = clock()
        polymult_int(function(*args))
        for arg in args:
            mult = polymult_int(function(mult, arg))
        time_2 = clock()
        return time_2 - time_1
    return wrapped


@times
@scaleofnotation
def create_random_numbers(start, end):
    from prime.randnum import Random
    rnd = Random()
    random = rnd.randrange(start, end)
    return random