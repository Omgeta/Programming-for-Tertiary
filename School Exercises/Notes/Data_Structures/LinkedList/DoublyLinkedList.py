class Node:
    def __init__(self, element):
        self.__data = element
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

