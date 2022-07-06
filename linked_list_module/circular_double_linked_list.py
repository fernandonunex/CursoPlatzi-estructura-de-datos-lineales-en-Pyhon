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
            if probe.data == data: # if the data is found, then return the pointer
                print(f"Data found {data}")
                return probe
            else:
                probe = probe.next
        
        probe = None # if the data is not found then return a pointer of None
        print(f"Data don't found {data}")

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

            probe = self.head # start at the head and is the index 0
            for _ in range(index):
                probe = probe.next
            return probe




    def size(self):
        """Return the size of the SinglyLinkedList"""
        return str(self._size)
