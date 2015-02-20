# notations


def scaleofnotation(number):                                # from notation 10 occured notation 2 ( result array)
    binary_array = []
    while number != 0:
        binary_array.append(number%2)
        number /= 2
    return binary_array


def backscaleofnotation(binary_array):                      # from notation 2 occurred notation 10 (result number)
    decimal_notation, iteration = 0, 1
    for bit in binary_array:
        decimal_notation += bit*iteration
        iteration *= 2
    return decimal_notation


def equal(a, around):
    doub = 2**around
    while len(a) != doub:
        a.append(0)
    return a