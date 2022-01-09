class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = [x for x in sequence]
        self.number = number
        self.index = 0
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations >= self.number:
            raise StopIteration

        if self.index >= len(self.sequence):
            self.index = 0
            value = self.sequence[self.index]
            self.index += 1
            self.iterations += 1
            return value
        else:
            value = self.sequence[self.index]
            self.index += 1
            self.iterations += 1
            return value


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')


