# Task 3.4
from typing import List
from datetime import date


class Todo:
    def __init__(self, due_date: date, category: str, description: str):
        self.due_date = due_date
        self._category = category
        self._description = description

    def set_category(self, c: str):
        self._category = c

    def set_description(self, description: str):
        self._description = description

    def set_due_date(self, due_date: date):
        self._due_date = due_date

    def get_category(self) -> str:
        return self._category

    def get_description(self) -> str:
        return self._description

    def get_due_date(self) -> date:
        return self._due_date

    def summary(self) -> str:
        return self.get_due_date() + " " + self.get_description() + ": " + self.get_description()

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

    def remove(self, todo: Todo):
        for i in range(len(self.data)):
            if todo.compare_with(self.data[i]) == 0:
                self.data.pop(i)


todo_list = TodoList()
with open("TASK3_3.txt", "r") as f:
    for line in f:
        due_date, category, description = line.rstrip("\n").split(" ")
        new_todo = Todo(due_date, category, description)
        todo_list.add(new_todo)

with open("TASK3_4.txt", "r") as f:
    for line in f:
        due_date, category, description = line.rstrip("\n").split(" ")
        new_todo = Todo(due_date, category, description)
        todo_list.remove(new_todo)
