import random


class Array:
    def __init__(self, capacity, fill_value=None):
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):  # None value defaults in range
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __fillRandom__(self, min=0, max=10):
        self.items = [random.randint(min, max) for i in range(self.capacity)]

    def __sumnumeric__(self):
        return sum(self.items)

    def __setitem__(self, index, new_item):
        self.items[index] = new_item
