from node import Node


class Stack:
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