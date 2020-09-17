class Queue:
    def __init__(self):
        self.__data = []

    def isempty(self):
        return (self.__data == [])

    def enqueue(self, value):
        self.__data.insert(0, value)

    def dequeue(self):
        return self.__data.pop()

    def peek(self):
        return self.__data[-1]

    def size(self):
        return len(self.__data)