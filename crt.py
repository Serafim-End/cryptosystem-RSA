from eea import *


def back_m_i(x, n):
    # Returns x^-1 (mod n)
    real, imagine, a = egcd(x, n)
    # if a != 1: raise ValueError("x (%d) and n (%d) are not relatively prime" % (x, n))
    return real


# Chinese Remainder Theorem
def crt(r_values, modulo_values):
    # Chinese Remainder Theorem.
    # returns: x such that x = r[i] (mod a[i]) for each i

    if len(modulo_values) <= 0 or len(r_values) <= 0:
        raise ValueError("arrays must not be empty")

    m = 1
    x = 0

    for modulo in modulo_values:
        m *= modulo

    for a_i, r_i in zip(modulo_values, r_values):
        m_i = m // a_i
        inv = back_m_i(m_i, a_i)
        x = (x + r_i * m_i * inv) % m

    return x
