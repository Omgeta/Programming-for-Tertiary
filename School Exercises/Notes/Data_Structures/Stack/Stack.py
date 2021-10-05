class Stack:
    """ Stack implementation for storing elements in LIFO order """

    def __init__(self, size: int = 32):
        """ Construct empty stack of specified size with head pointed at first empty element """
        self.size = size
        self.data = [None] * self.size
        self.head = 0

    def is_empty(self) -> bool:
        """ Checks if a stack is empty """
        return self.head == 0

    def push(self, value: any):
        """ Push a value onto the stack and increment the head pointer """
        if self.head == self.size:
            print("Stack has reached full capacity! Unable to add any more elements")
        else:
            self.data[self.head] = value
            self.head += 1

    def pop(self) -> any:
        """ Pop a value from the top of the stack and decrement the head pointer """
        if self.is_empty():
            print("Stack is empty! Unable to remove any more elements!")
        else:
            self.head -= 1
            value = self.data[self.head]
            self.data[self.head] = None  # let the GC handle deletion
            return value

    def peek(self) -> any:
        """ Peek at a value from the top of the stack without removing it """
        if self.is_empty():
            print("Stack is empty! Unable to view any more elements!")
        else:
            self.head -= 1
            value = self.data[self.head]
            self.head += 1
            return value
