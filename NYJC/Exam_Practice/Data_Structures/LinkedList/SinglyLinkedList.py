class Node:
    def __init__(self, element):
        self.__data = element
        self.next = None

    def islast(self):
        return (self.next is None)



class LinkedList:
    def __init__(self):
        self.root = None

    def isempty(self):
        return (self.root is None)

    def get(self, index):
        current = self.root
        j = 0
        while j < index and current is not None:
            current = current.next
            j += 1
            
        return current

    def insert(self, index, element):
        previous, current = None, self.root
        j = 0
        while j < index and current is not None:
            previous, current = current, current.next
            j += 1

        new_node = Node(element)
        new_node.next = current

        if previous is None:
            self.root = new_node
        else:
            previous.next = new_node

    def append(self, element):
        new_node = Node(element)

        current = self.root
        if current is None:
            current = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self, index):
        previous, current = None, self.root
        j = 0
        while j < index and current is not None:
            previous, current = current, current.next
            j += 1
        
        if previous is None:
            self.root = current.next
        else:
            previous.next = current.next

