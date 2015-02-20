# decorator for correct numbers
def correct_data(function):
    def wrapped(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return function(a, b)
        else:
            try:
                a, b = int(a), int(b)
                return function(a, b)
            except ValueError:
                return "Incorrect data"
    return wrapped


# Euclidian Algorithm
@correct_data
def gcd(a, b):                  # someone say that it in 2.8 faster than egcd(a,b)[2] and i think that it is obvious
    while b:
        if a < b:
            a, b = b, a
        a, b = b, (a % b)
    return a


# Extended Euclidian Algorith
@correct_data
def egcd(a, b):
    # Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    # r = gcd(a,b) i = multiplicative inverse of a mod b
    #      or      j = multiplicative inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively

    y, x = (1, 0)
    real, imagine = (1, 0)
    a_start, b_start = a, b                                                # Remember original a/b to remove

    while b:
        q = a // b
        a, b = b, (a % b)

        real, x = x, (real - (q * x))
        imagine, y = y, (imagine - (q * y))

    if real < 0:
        real += b_start                                                     # If neg wrap modulo original b
    if imagine < 0:
        imagine += a_start                                                  # If neg wrap modulo original a
    return real, imagine, a              # Return only positive values -- for this the method was overrode