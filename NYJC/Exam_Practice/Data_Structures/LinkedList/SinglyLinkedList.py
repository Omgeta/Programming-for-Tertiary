class Node:
    def __init__(self, value=any, next: Node = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self) -> bool:
        return (self.head is None)

    def add(self, value: any):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node

    def get(self, index: int) -> any:
        ptr = self.head
        j = 0
        while j < index and ptr is not None:
            ptr = ptr.next
            j += 1

        return ptr

    def insert(self, index: int, value: any):
        prevPtr, ptr = None, self.head
        j = 0
        while j < index and ptr is not None:
            prevPtr, ptr = ptr, ptr.next
            j += 1

        new_node = Node(value)
        new_node.next = ptr

        if prevPtr is None:
            self.head = new_node
        else:
            prevPtr.next = new_node

    def delete(self, index: int):
        prevPtr, ptr = None, self.head
        j = 0
        while j < index and ptr is not None:
            prevPtr, ptr = ptr, ptr.next
            j += 1

        if prevPtr is None:
            self.head = ptr.next
        else:
            prevPtr.next = ptr.next
