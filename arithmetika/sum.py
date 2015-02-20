

class SumAndDifference(object):
    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two
        temp = len(self.number_one) - len(self.number_two)

        def appending(first, second):
            while len(first) != len(second):
                second.append(0)
            return first, second

        if temp > 0:
            self.number_one, self.number_two = appending(self.number_one, self.number_two)
        if temp < 0:
            self.number_two, self.number_one = appending(self.number_two, self.number_one)

    def sum(self):
        try:
            if isinstance(self.number_one, list) and isinstance(self.number_two, list):
                iter_plus = [0]
                n = len(self.number_one)
                for i in xrange(n):
                    iter_plus.append((self.number_one[i] + self.number_two[i] + iter_plus[i]) >> 1)
                    self.number_one[i] = (self.number_one[i] + self.number_two[i] + iter_plus[i]) % 2
                if iter_plus[n] != 0:
                    self.number_one.append(iter_plus[n])
                return self.number_one
        except ValueError:
            raise Exception("type of entered data was not correct")

    def difference(self):
        try:
            if isinstance(self.number_one, list) and isinstance(self.number_two, list):
                iteration = 0
                for n_from, n_what in zip(self.number_one, self.number_two):
                    temp = n_from - n_what

                    if temp >= 0:
                        self.number_one[iteration] = temp
                    else:
                        i = 1
                        while True:
                            if self.number_one[iteration + i] == 1:
                                self.number_one[iteration + i] = 0
                                break
                            i += 1
                        self.number_one[iteration] = 1
                    iteration += 1
                return self.number_one
        except ValueError:
            print "type ofd entered data was not correct"


def sum(binary_one, binary_two):
    obj = SumAndDifference(binary_one, binary_two)
    return obj.sum()