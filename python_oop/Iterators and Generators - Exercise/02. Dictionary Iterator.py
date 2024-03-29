class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dict(dictionary)
        self.index = 0
        self.keys = list(self.dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dictionary):
            raise StopIteration

        key = self.keys[self.index]
        value = self.dictionary[key]

        self.index += 1
        return key, value
