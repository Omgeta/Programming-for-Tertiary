# Task 3.2
from typing import List


class Todo:
    def __init__(self, category: str, description: str):
        self._category = category
        self._description = description

    def set_category(self, c: str):
        self._category = c

    def set_description(self, description: str):
        self._description = description

    def get_category(self) -> str:
        return self._category

    def get_description(self) -> str:
        return self._description

    def summary(self) -> str:
        return self.get_description() + ": " + self.get_description()

    def compare_with(self, td: 'Todo') -> int:
        if self.summary() < td.summary():
            return -1
        elif self.summary() > td.summary():
            return 1
        else:
            return 0


class TodoList:
    def __init__(self):
        self.data = []

    def isempty(self) -> bool:
        return len(self.data) == 0

    def contents(self) -> List[Todo]:
        return self.data

    def add(self, todo: Todo):
        if self.isempty():
            self.data.append(todo)
        else:
            if todo.compare_with(self.data[-1]) > 0:
                self.data.append(todo)
            elif todo.compare_with(self.data[0]) < 0:
                self.data.insert(0, todo)
            else:
                found = False
                j = 0
                while not found and j <= len(self.data):
                    if todo.compare_with(self.data[j]) >= 0 and todo.compare_with(self.data[j+1]) < 0:
                        found = True
                        self.data.insert(j+1, todo)


todo_list = TodoList()
with open("TASK3_2.txt", "r") as f:
    for line in f:
        category, description = line.rstrip("\n").split(" ")
        new_todo = Todo(category, description)
        todo_list.add(new_todo)

for todo in todo_list.contents():
    print(todo.summary())
