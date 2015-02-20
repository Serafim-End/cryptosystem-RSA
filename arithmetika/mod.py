
class IModalByModal:
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

    def modal(self):
        pass


class ModalByModal(IModalByModal):
    def __init__(self,number_one,number_two):
        IModalByModal.__init__(self, number_one, number_two)

    def modal(self):
        return

