"""Module to model nodes"""

class Node():
    """Structure of a node, has data and the next reference
    to another node."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        super().__init__(data, next)
        self.previous = previous