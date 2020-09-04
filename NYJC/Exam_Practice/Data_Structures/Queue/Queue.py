class Queue:
    def __init__(self):
        self.__data = []

    def isempty(self):
        return (self.__data == [])

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self):
        return self.data.pop()

    def size(self):
        return len(self.__data)