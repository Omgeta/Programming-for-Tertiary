class CircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.__data = [None] * self.size
        self.head = None

    def isempty(self):
        return (self.head is None)

    def enqueue(self, value):
        if self.isempty():
            self.head = 0
        else:
            self.head = (self.head + 1) % self.size
        self.__data[self.head] = value

    def dequeue(self):
        if self.isempty():
            print("Error: CircularQueue is empty")
        else:
            value = self.__data[self.head]
            self.__data[self.head] = None

            if self.head == 0:
                self.head = self.size - 1
            else:
                self.head -= 1

            if self.__data[self.head] is None:
                self.head = None

            return value
