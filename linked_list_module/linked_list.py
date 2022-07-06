"""Module of a Singly Linked List data structure"""
from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None  # the tail is the last node
        self.size = 0

    def append(self, data):
        """Append a node to the singly linked list
            the tail is te first node always, this way
            tail(node)-node-node-head(node)

            data(any type) = could be a string, number, etc.
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
            yield val  # generators of val

    def delete(self, data):
        """This method delete the references to the node,
            this node exist but we cant reach it because
            there is no more references to it. Jump the node
        """
        current = self.tail  # current node
        previous = self.tail  # previous node

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
        probe = self.tail

        while probe != None and data != probe.data:
            probe = probe.next

        if probe != None:
            print(f"Data {data} has been found")
        else:
            print(f"Data {data} is not in the linked list")

    def clear(self):
        """Clear the SinglyLinkedList by cleaning the head and tail
            let sat, point to nowhere. 
        """
        self.tail = None
        self.head = None
        self.size = 0

    def array_to_linked(self, arr):
        """Create a Singly Linked List from an array of one dimension"""
        for item in arr.__iter__():
            self.append(item)

    def show_linked_list(self):
        """
        Print all the data of the linked list, the first element
        element is the head and the last is the tail.
        """
        probe = self.tail
        while probe != None:
            print(probe.data)
            probe = probe.next

    def replace_item(self, target_item, new_item):
        """Replace an item(data) from the linked list with the item(data)
        passed in the argument of the method.
        Just replace the first item that match the target_item.

        Args:
            target_item (int,str,float): data to replace the old data in linked list
        """
        probe = self.tail

        while probe != None and target_item != probe.data:
            probe = probe.next

        if probe != None:
            probe.data = new_item
            print(
                f"{new_item} replaced the old value in the node number {target_item}")
        else:
            print(f"The target item {target_item} is not in the linked list")

    def insert_at_head(self, new_item):
        """Insert a new node at head of the linked list

        Args:
            new_item (any): this is the data of the new node that will be
            at the head
        """
        new_node = Node(new_item)  # Create a node with the data from args

        if self.tail is None:
            self.tail = new_node
        else:
            probe = self.tail
            while probe.next != None:
                probe = probe.next
            probe.next = new_node

    def remove_the_head(self):
        """Remove the item at the head"""
        removed_item = self.tail
        if self.tail.next is None:
            self.tail = None
        else:
            probe = self.tail
            while probe.next.next != None:
                probe = probe.next
            removed_item = probe.next.data
            probe.next = None

        print(f"--> {removed_item}")

    def insert_in_index(self, new_item, index):
        """Insert a node with a specific data and in a specific index.
        The index is counting from tail to head and start in 0

        Args:
            new_item (any): data to be stored in the node
            index (int): index to insert the node 0 - tail, 
            index > 0 from tail to head.  
        """
        if self.tail is None or index <= 0:
            self.tail = Node(new_item, self.tail)
        else:
            probe = self.tail
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(new_item, probe.next)

    def delete_from_index(self, index: int) -> None:
        """Delete a node in a specified index

        Args:
            index (int): start counting form 0 and at the tail. 
            index [0] is the tail   
        """

        if index <= 0 or self.tail.next is None:
            removed_item = self.tail.data
            self.tail = self.tail.next
            print(f"Item removed: {removed_item}")
        else:
            probe = self.tail
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removed_item = probe.next.data
            probe.next = probe.next.next
            print(f"Item removed: {removed_item}")
