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
        if self.head == None:  # If there is nothing in head, then it will be head
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

    def reverse_iter(self):
        """Return the data of every node form tail to head"""
        if self.tail == None:
            return print("The circular double linked list is empty")
        else:
            probe = self.tail

            while probe != self.head:
                yield probe.data
                probe = probe.previous
            yield probe.data

    def _get_node_by_data(self, data):
        """Search an item by the data stored in it, starting from the head to tail
            Makes match with the first item found
            If is found then will return the pointer"""
        probe = self.head
        for _ in range(int(self.size())):
            if probe.data == data:  # if the data is found, then return the pointer
                return probe
            else:
                probe = probe.next

        probe = None  # if the data is not found then return a pointer of None

        return probe

    def _get_node_by_index(self, index):
        """Get a node by index, start counting from 0 (is the head) and
            finish in n (is the tail)
            If index > self._size then return the self.tail 
            If index < 0 then return the self.head
        """
        # check out if the index is bigger than the size of the circular double list
        if index >= int(self.size()):
            probe = self.tail
            return probe

        elif index <= 0:
            probe = self.head
            return probe

        else:

            probe = self.head  # start at the head and is the index 0
            for _ in range(index):
                probe = probe.next
            return probe

    def delete_node_by_data(self, data):
        """Search a node using an argument 'data', then change
        the pointers to the node, so it will disapear form the linked list."""
        probe = self._get_node_by_data(data)
        if probe != None:
            if probe == self.tail:  # this code is to dont lose the tail
                self.tail = probe.previous
                self._link_head_to_tail()
            elif probe == self.head:  # this code is to dont lose the head
                self.head = probe.next
                self._link_head_to_tail()
            else:
                self._insert_node_between(probe.previous, probe.next)
            print(f"Removed: {data}")
        else:
            print(f"The data '{data}' was not found.")

    def show_data(self):
        """Print the data of each node, from head to tail one time"""

        for data in self.iter():
            print(data)

    def size(self):
        """Return the size of the SinglyLinkedList"""
        return str(self._size)
