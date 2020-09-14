class Node:
    def __init__(self, element):
        self.__data = element
        self.next = None

    def islast(self):
        return (self.next is None)



class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        return (self.head is None)

    def get(self, index):
        current = self.head
        j = 0
        while j < index and current is not None:
            current = current.next
            j += 1
            
        return current

    def insert(self, index, element):
        previous, current = None, self.head
        j = 0
        while j < index and current is not None:
            previous, current = current, current.next
            j += 1

        new_node = Node(element)
        new_node.next = current

        if previous is None:
            self.head = new_node
        else:
            previous.next = new_node

    def append(self, element):
        new_node = Node(element)

        current = self.head
        if current is None:
            current = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self, index):
        previous, current = None, self.head
        j = 0
        while j < index and current is not None:
            previous, current = current, current.next
            j += 1
        
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

