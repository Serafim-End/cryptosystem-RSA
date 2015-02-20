from RSA import *
from key import GetKeys

# interactive tests


class Main():
    def __init__(self, bits_numb):
        self.bits_numb = bits_numb
        self.main()

    def positive_number(self):
        if self.bits_numb <= 4:
            print 'You entered number of bits smaller than 4, but 4 it is a minimum!'
            return True
        return False

    @staticmethod
    def equals(message, decrypt):
        return message == decrypt

    def wait_please(self):
        if self.bits_numb > 1024:
            print "wait please"
        return

    def create_keys(self):
        return GetKeys.get_keys(self.bits_numb)

    @staticmethod
    def message_input():
        message = raw_input("message: ")
        return message

    def gen_key(self):
        return self.create_keys()

    @staticmethod
    def encrypt_decrypt(public, private, message, crypt_decrypt=True):
        if crypt_decrypt:
            return Crypt.encrypt(message, public)
        else:
            return Crypt.decrypt(message, private)

    def main(self):
        if self.positive_number():
            self.wait_please()
            public, private = self.gen_key()

            message = self.message_input()
            encrypt = self.encrypt_decrypt(public, private, message, True)
            decrypt = self.encrypt_decrypt(public, private, encrypt, False)

            if self.equals(message, decrypt):
                print 'e: ', public['e'], \
                    '\nn: ', public['n'], \
                    '\nd: ', private['d']
                print encrypt
                print decrypt
            return
        else:
            raise Exception("Error")


def main(bits_numb):

    if bits_numb >= 1024:
        print 'Wait please!'
    if bits_numb < 8:
        print "You entered number of bits smaller than 8, but 8 it is a minimum!"

    else:
        public, private = GetKeys.get_keys(bits_numb)
        print
        message = raw_input('message: ')

        encrypted = Crypt.encrypt(message, public)
        decrypted = Crypt.decrypt(encrypted, private)

        if Main.equals(message, decrypted):
            print 'e: ', public['e'], \
                '\nn: ', public['n'], \
                '\nd: ', private['d']
            print encrypted
            print decrypted

    return

if __name__ == '__main__':
    n = input("Enter number of bits: ")
    main(n)