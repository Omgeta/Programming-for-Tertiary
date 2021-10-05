class LinearQueue:
    """ LinearQueue implementation which stores elements in a FIFO order """

    def __init__(self):
        """ Initializes dynamic array to store elements """
        self.data = []

    def is_empty(self):
        """ Checks if the queue is empty """
        return self.size() == 0

    def enqueue(self, value: any):
        """ Enqueues an element in the end of the queue """
        self.data.append(value)

    def dequeue(self) -> any:
        """ Dequeues and returns an element from the front of the queue """
        return self.data.pop(0)

    def peek(self) -> any:
        """ Peek at the element in the front of the queue """
        return self.data[0]

    def size(self):
        return len(self.data)
