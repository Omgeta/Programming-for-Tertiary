# Task 4.2
from typing import List


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = self._create_grid(self.width, self.height, 46)

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

    def replace_point(self, x, y, char):
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
x_pos = int(input(f"X coordinate <1 to {g.width}>? ").strip())
y_pos = int(input(f"Y coordinate <1 to {g.height}>? ").strip())
g.replace_point(x_pos, y_pos, 83)
g.display()
