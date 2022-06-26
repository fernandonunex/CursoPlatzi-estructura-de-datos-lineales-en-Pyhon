from array_ import Array
from grid import Grid
import random


class Cube(object):

    def __init__(self, rows, columns, cells, fill_value=None):
        self.rows = rows
        self.columns = columns
        self.cells = cells
        self.data = Grid(rows, columns, fill_value)
        for row in range(rows):
            for col in range(columns):
                for cell in range(cells):
                    self.data[row][col] = Array(cells, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def get_deep(self):
        return len(self.data[0][0])

    def __getitem__(self, row, col, cell):
        return self.data[row][col][cell]

    def __fillRandom__(self, min=0, max=10):
        for row in range(self.rows):
            for col in range(self.columns):
                for cell in range(self.cells):
                    self.data[row][col][cell] = random.randint(min, max)

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += "["
                for cell in range(self.get_deep()):
                    result += str(self.data[row][col][cell])+" "
                result += "]\n"
            result += "\n"
        return str(result)

