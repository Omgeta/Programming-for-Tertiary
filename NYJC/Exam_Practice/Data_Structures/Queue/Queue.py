class Queue:
    def __init__(self):
        self.data = []

    def isempty(self) -> bool:
        return (self.data == [])

    def enqueue(self, value: any):
        self.data.insert(0, value)

    def dequeue(self) -> any:
        return self.data.pop()

    def peek(self) -> any:
        return self.data[-1]

    def size(self) -> int:
        return len(self.data)
