class CircularQueue:
    """ Circular Queue implementation which stores elements in a FIFO order of fixed size """

    def __init__(self, size: int = 32):
        """ Constructs a static array to hold elements in a fixed size with head pointing at the first element"""
        self.size = size
        self.data = [None] * self.size
        self.head = None

    def is_empty(self):
        """ Checks if the queue is empty """
        return self.head is None

    def enqueue(self, value: any):
        """ Enqueues an element to the end of the queue, overwriting the oldest elements if max size is reached """
        if self.is_empty():
            self.head = 0
        else:
            # increment head and wrap around if too large
            self.head = (self.head + 1) % self.size

        self.data[self.head] = value

    def dequeue(self) -> any:
        """ Dequeues an element from the front of the queue """
        if self.is_empty():
            print("Queue is empty. Cannot pop any more elements")
            return None

        # get value and set it to None for GC to delete it
        value = self.data[self.head]
        self.data[self.head] = None

        # decrement head and wrap around if too small
        self.head = (self.head - 1) % self.size

        # revert queue to empty state if there are no more elements left in the whole queue
        if self.data[self.head] is None:
            self.head = None

    def peek(self) -> any:
        """ Peeks at an element from the front of the queue """
        if self.is_empty():
            print("Queue is empty. Cannot pop any more elements")
            return None

        return self.data[self.head]
