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
            self.tail.previous = self.head
            self._link_head_to_tail()
        # after making the circular double linked list then we are adding the new
        # node to the tail and creating the bridge to the head in both ways
        else:
            probe = self.tail
            self._insert_node_between(probe, node)
            self.tail = node
            self._link_head_to_tail()

        self._size += 1


    def _link_head_to_tail(self):
        """Making a method to link the tail to the head int both ways"""
        self.head.previous = self.tail
        self.tail.next = self.head
    
    def _insert_node_between(self, node_previous, node_next):
        """Insert a node between another nodes"""
        node_previous.next = node_next
        node_next.previous = node_previous

    def iter(self):
        """Return the data of every node form head to tail"""
        if self.head == None:
            return print("The circular double linked list is empty")
        else:
            probe = self.head

            while probe != self.tail:
                yield probe.data
                probe = probe.next
            yield probe.data

    def size(self):
        """Return the size of the SinglyLinkedList"""
        return str(self._size)
