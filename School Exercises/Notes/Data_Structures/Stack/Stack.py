class Stack:
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * self.size
        self.head = 0

    def isempty(self) -> bool:
        return self.head == 0

    def push(self, value: any):
        if self.head >= self.size:
            print("Stack capacity is reached!")
        else:
            self.data[self.head] = value
            self.head += 1

    def pop(self) -> any:
        if self.isempty():
            print("Stack is empty!")
        else:
            self.head -= 1
            value = self.data[self.head]
            self.data[self.head] = None
            return value

    def peek(self, value: any) -> any:
        if self.isempty():
            print("Stack is empty")
        else:
            self.head -= 1
            value = self.data[self.head]
            self.head += 1
            return value
