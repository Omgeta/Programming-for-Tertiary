# Task 4.2
from typing import List
from random import randint


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = self._create_grid(self.width, self.height, 46)
        self._add_fish(3)

    @staticmethod
    def _create_grid(width: int, height: int, fillchar: str = None) -> List[List]:
        """
        Create an empty 2D array grid

        Args:
            width: Width of the array
            height: Height of the array
        Returns:
            2D array of size width * height
        """
        grid = []
        for _ in range(width):
            grid.append([fillchar] * height)
        return grid

    def _add_fish(self, n: int):
        """
        Randomly add 3 fish to the pond

        Args:
            n: number of fish to add
        """
        FISH_CHAR = 70

        for _ in range(n):
            i, j = None, None
            while (not i) or (not j) or self.at(i, j) == FISH_CHAR:
                i = randint(1, self.width)
                j = randint(1, self.height)
            self.replace_point(i, j, FISH_CHAR)

    def at(self, x: int, y: int) -> int:
        """
        Get point in the grid (1 to x) * (1 to y).

        Args:
            x: x coordinate to get
            y: y coordinate to get
        Returns:
            Value at the point
        """
        return self.data[x-1][y-1]

    def replace_point(self, x: int, y: int, char: str):
        """
        Replace point in grid (1 to x) * (1 to y) with a character

        Args:
            x: x coordinate of point to replace
            y: y coordinate of point to replace
            char: character to replace with
        """
        self.data[x-1][y-1] = char

    def display(self):
        """
        Display grid contents
        """
        res = ""
        for j in range(self.height):
            for i in range(self.width):
                res += chr(self.data[i][j])  # Convert each code to a character
            res += "\n"
        print(res)


g = Grid(15, 8)
g.display()
