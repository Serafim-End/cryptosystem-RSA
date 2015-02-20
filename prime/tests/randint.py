from prime.prime import Prime


def tests(minvalue, maxvalue, tests_number):
    return [Prime.randintMyRandom(minvalue, maxvalue)
            for i in xrange(tests_number)]


def main():
    min_value = 10
    max_value = 1000
    tests_number = 100

    array = tests(min_value, max_value, tests_number)
    for randNumb in array:
        print randNumb

if __name__ == '__main__':
    main()