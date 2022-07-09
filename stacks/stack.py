from node import Node
from array_ import Array


class Stack:
    """Stack data structure based in nodes"""

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return "The stack is empty"

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        while self.top:
            self.pop()

    def clear_v2(self):
        self.__init__()

    def iter(self):
        probe = self.top
        while probe != None:
            yield probe.data
            probe = probe.next

    def search(self, data):
        if self.top:
            for data_stored in self.iter():
                if data_stored == data:
                    return f"Data '{data}' found"
            return f"Data '{data}' do not  found"
        else:
            return "The stack is empty"


class Stack_list():
    """Stack data structure based in arrays"""

    def __init__(self, size):
        """Create the Sack based in arrays

        Args:
            size (int): the size or capacity of the stack
        """
        self.top = None
        self.items = Array(size)
        self._size = size
        self._counter = 0  # to know where is the top

    def push(self, data):

        if self._counter < self._size:
            self.items.__setitem__(self._counter, data)
            self._counter += 1
        else:
            return f"The stack is full, the item '{data}' was not added"

    def iter(self):
        """Returns each element, form top to bottom (FIFO)"""
        for index in range(self._counter-1, -1, -1):
            yield self.items.__getitem__(index)

    def pop(self):
        """Returns the peek element and deletes form the stack
            if is empty then returns a string saying the stack is empty
        """
        if self._counter > 0:
            element = self.items.__getitem__(self._counter-1)
            self.items.__setitem__(self._counter-1, None)
            self._counter -= 1
        else:
            return "The stack is empty"
        return element

    def clear(self):
        """Clear the stack, set all the items with None value and
            set the _counter to 0"""
        self.__init__(self._size)

    def search(self, target):
        """Search if a specific data is in the stack and returns the index (int) of the item
            and if the data was not find then returns a None value
            """
        if self._counter > 0:
            index = -1
            for data in self.iter():
                index += 1
                if data == target:
                    print(f"Data '{target}' found")
                    return self._counter-index
            else:
                print(f"Data '{target}' did not find")
                return None
        else:
            print("The stack is empty")
            return None 