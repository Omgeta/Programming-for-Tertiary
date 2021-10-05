class Node:
    """ Utility class for LinkedList which holds element and pointer to the next node in the list """

    def __init__(self, value: any, next: 'Node' = None):
        self.value = value
        self.next = next


class LinkedList:
    """ Singly LinkedList implementation which stores nodes linked to the next node"""

    def __init__(self, head: Node = None):
        """ Holds first node in the linked list """
        self.head = head

    def add(self, value: any):
        """ Adds node to the end of the linked list """
        # create new node
        new_node = Node(value)

        # set as head if list is empty
        if self.head is None:
            self.head = new_node
        else:
            # iterate through remaining nodes until last one is found
            prev, curr = None, self.head

            while curr is not None:
                prev, curr = curr, curr.next

            # set next of last node to point at the new_node
            prev.next = new_node

    def insert(self, index: int, value: any):
        """ Inserts node into a specified index in the linked list """
        # create the new node
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            # iterate through specified number of nodes until end is found or the index is found
            prev, curr = None, self.head
            j = 0

            while j < index and curr is not None:
                prev, curr = curr, curr.next
                j += 1

            # link new_node to the node that was at the index before
            new_node.next = prev.next
            # link prev node to new_node instead of the ndoe that was at the index before
            prev.next = new_node

    def edit(self, index: int, new_value: any):
        """ Edits node at the index to new value """
        # iterate through specified number of nodes until end or index is found
        prev, curr = None, self.head
        j = 0

        while j < index and curr is not None:
            prev, curr = curr, curr.next
            j += 1

        # only modify if we are at the correct index
        if j == index:
            # do not modify if we are at the start, and head is pointing at None
            if prev is not None or self.head is not None:
                curr.value = new_value

    def remove(self, index: int):
        """ Removes a node from the index """
        # iterate through specified number of nodes until end or index is found
        prev, curr = None, self.head
        j = 0

        while j < index and curr is not None:
            prev, curr = curr, curr.next
            j += 1

        # only remove if we are at the correct index
        if j == index:
            # if we are removing head, set it to be None
            if prev is None:
                self.head = None
            else:  # linked prev node to the next node after the current, and delete the current
                prev.next = curr.next
                del curr

    def get(self, index: int):
        """ Gets the node at the given index """
        prev, curr = None, self.head
        j = 0

        while j < index and curr is not None:
            prev, curr = curr, curr.next
            j += 1

        # only get if we are at the correct index
        if j == index:
            if prev is not None or self.head is not None:
                return curr.value
