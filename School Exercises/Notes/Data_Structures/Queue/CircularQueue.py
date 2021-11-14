class CircularQueue:
    """ Circular Queue implementation which stores elements in a FIFO order of fixed size """

    def __init__(self, size: int = 32):
        """ Constructs a static array to hold elements in a fixed size with head pointing at the first element"""
        self.size = size
        self.data = [None] * self.size
        self.head = None
        self.tail = None

    def is_empty(self):
        """ Checks if the queue is empty """
        return self.head is None

    def enqueue(self, value: any):
        """ Enqueues an element to the next free spot in the queue """
        if (self.tail + 1) % self.size == self.front:
            print("Queue is full")
        elif self.is_empty():
            self.head = 0
            self.tail = 0
            self.data[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.size
            self.data[self.tail] = value

    def dequeue(self) -> any:
        """ Dequeues an element from the front of the queue """
        if self.is_empty():
            print("Queue is empty. Cannot pop any more elements")
        elif self.head == self.tail:
            res = self.data[self.head]
            self.head = None
            self.tail = None
            return res
        else:
            res = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return res

    def peek(self) -> any:
        """ Peeks at an element from the front of the queue """
        if self.is_empty():
            print("Queue is empty. Cannot pop any more elements")
            return None

        return self.data[self.head]
