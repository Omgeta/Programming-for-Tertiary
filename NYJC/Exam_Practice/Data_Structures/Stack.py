class Stack:
    def __init__(self, size=30):
        self.size = size
        self.data = [None] * self.size
        self.head = 0

    def isempty(self):
        return (self.head == 0)

    def push(self, value):
        if self.head >= self.size:
            print("Error: stack capacity reached")
        else:
            self.data[self.head] = value
            self.head += 1

    def pop(self):
        if self.isempty():
            return None
        else:
            self.head -= 1
            return self.data.pop(self.head)

    