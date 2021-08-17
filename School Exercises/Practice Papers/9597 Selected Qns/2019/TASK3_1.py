# Task 3.1
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
