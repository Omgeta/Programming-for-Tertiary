class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.__data = [None] * self.size

    def __hash(self, string):
        index = hash(string)
        if index < 0:
            index = index % (self.size // 2)
        else:
            index = index % (self.size // 2) + (self.size // 2)
        return index

    def add(self, key, value):
        index = self.__hash(key)
        self.__data[index] = value

    def get(self, key):
        index = self.__hash(key)
        return self.__data[index]