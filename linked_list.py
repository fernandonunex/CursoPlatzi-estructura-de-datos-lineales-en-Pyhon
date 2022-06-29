"""Module of a Singly Linked List data structure"""
from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None  # the tail is the last node
        self.size = 0

    def append(self, data):
        """Append a node to the singly linked list
            the tail is te first node always, this way
            tail(node)-node-node-head
        """
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    def size(self):
        """Return the size of the SinglyLinkedList"""
        return str(self.size)

    def iter(self):
        """Create a iterator to return each node
            from tail to head.    
        """
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val # generators of val

    def delete(self, data):
        """This method delete the references to the node,
            this node exist but we cant reach it because
            there is no more references to it. Jump the node
        """
        current = self.tail # current node
        previous = self.tail # previous node

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

            previous = current
            current = current.next

    def search(self, data):
        """Search a specific data of a node in the 
        SinglyLinkedList data structure.

        Args:
            data (int, str, bolean, etc): any data that could
            be store in a variable 
        """
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")

    def clear(self):
        """Clear the SinglyLinkedList by cleaning the head and tail
            let sat, point to nowhere. 
        """
        self.tail = None
        self.head = None
        self.size = 0

    