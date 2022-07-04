"""Module to data structure: Circle Double Linked List"""
from node import TwoWayNode


class CircleDoubleLinkedList():
    """Data structure of two way nodes (double)"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        """Append a node to the tail"""
        node = TwoWayNode(data)
        if self.head == None: # If there is nothing in head, then it will be head
            self.head = node
        # if there is something in head but not in tail, then it will be tail
        # and then we can make the circular double linked list
        elif self.tail == None: 
            self.tail = node
            self.head.next = self.tail
            self.head.previous = self.tail
            self.tail.previous = self.head
            self.tail.next = self.head
        # after making the circular double linked list then we are adding the new
        # node to the tail and creating the bridge to the head in both ways
        else:
            probe = self.tail
            probe.next = node
            node.previous = probe
            node.next = self.head
            self.head.previous = node
            self.tail = node

        self._size += 1


    def size(self):
        """Return the size of the SinglyLinkedList"""
        return str(self._size)
