"""Module to create an array 2 dimensional"""

from array_ import Array

class Grid():
    """Array of 2 dimensions"""
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def __len__(self):
        """Return the len of rows"""
        return len(self.data)

    def get_height(self):
        """Return the len of rows"""
        return len(self.data)

    def get_width(self):
        """Return the len of columns"""
        return len(self.data[0])

    def __getitem__(self, index):
        """Return the an item given a index"""
        return self.data[index]

    def __str__(self):
        """Representation of the data in str in the 
        data structure 
        """
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col])+" "
            result += "\n"

        return str(result)
