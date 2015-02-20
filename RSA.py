from convert import *


class ChipsIntoChops:
    def __init__(self):
        pass

    @staticmethod
    def encode64chops(chops):
        chips = []  # chips are character chops
        for value in chops:
            chips.append(int2str64(value))
        encoded = ','.join(chips)
        return encoded

    @staticmethod
    def decode64chops(string):
        chips = string.split(',')  # split chops at commas
        chops = []
        for string in chips:  # make char chops (chips) into chops
            chops.append(str642int(string))
        return chops

    @staticmethod
    def chopstring(message, key, n, func):
        msglen = len(message)
        # mbits = msglen * 8
        nbits = bit_size(n) - 2  # leave room for safebit
        nbytes = nbits / 8
        blocks = msglen / nbytes

        if msglen % nbytes > 0:
            blocks += 1

        cypher = []

        for bindex in range(blocks):
            offset = bindex * nbytes
            block = message[offset:offset + nbytes]
            value = bytes2int(block)
            cypher.append(func(value, key, n))
        return ChipsIntoChops.encode64chops(cypher)  # Encode encrypted ints to base64 strings


class CryptInt:
    def __init__(self):
        pass

    @staticmethod
    def encrypt_int(message, ekey, n):
        if isinstance(message, types.IntType):
            message = long(message)

        if not isinstance(message, types.LongType):
            raise TypeError("You must pass a long or int")

        if message < 0 or message > n:
            raise OverflowError("The message is too long")

        safebit = bit_size(n) - 2  # compute safe bit (MSB - 1)
        message += (1 << safebit)  # add safebit to ensure folding
        return pow(message, ekey, n)

    @staticmethod
    def decrypt_int(cyphertext, dkey, n):
        message = pow(cyphertext, dkey, n)
        safebit = bit_size(n) - 2  # compute safe bit (MSB - 1)
        message -= (1 << safebit)  # remove safebit before decode
        return message


class Crypt:
    def __init__(self):
        pass

    @staticmethod
    def gluechops(string, key, n, func):
        message = ""
        chops = ChipsIntoChops.decode64chops(string)  # Decode base64 strings into integer chops
        for cpart in chops:
            mpart = func(cpart, key, n)  # Decrypt each chop
            message += int2bytes(mpart)  # Combine decrypted strings into a msg
        return message

    @staticmethod
    def encrypt(message, key):
        if 'n' not in key:
            raise Exception("You must use the public key with encrypt")
        return ChipsIntoChops.chopstring(message, key['e'], key['n'], CryptInt.encrypt_int)

    @staticmethod
    def sign(message, key):
        if 'p' not in key:
            raise Exception("You must use the private key with sign")
        return ChipsIntoChops.chopstring(message, key['d'], key['p'] * key['q'], CryptInt.encrypt_int)

    @staticmethod
    def decrypt(cypher, key):
        if 'p' not in key:
            raise Exception("You must use the private key with decrypt")
        return Crypt.gluechops(cypher, key['d'], key['p'] * key['q'], CryptInt.decrypt_int)
