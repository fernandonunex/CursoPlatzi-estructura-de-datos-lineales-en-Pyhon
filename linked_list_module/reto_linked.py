from node import Node
from array_ import Array
from linked_list import SinglyLinkedList


def run():
    # 1. Code to create a method to convert form a list to a linked list

    # random_int = Array(5)
    # random_int.__fillRandom__()
    # print(random_int)
    
    # random_int_linked = SinglyLinkedList()

    # print("Creating the random_int_linked")
    # for num in random_int.__iter__():
    #     random_int_linked.append(num)

    # print("Printing all the created nodes in the linked list")
    # for random in random_int_linked.iter():
    #     print(random)

    # 2. Code to understand a circular linked list

    # index = 1

    # new_item = 'ham'
    # head = Node(None, None)
    # head.next = head
    # probe = head
    # while index > 0 and probe.next != head:
    #     probe = probe.next
    #     index -= 1
    
    # probe.next = Node(new_item, probe.next)
    # print(probe.data)
    # print(probe.next.data)
    # print(probe.next.next.data)
    # print(probe.next.next.next.data)

    # 2.1 Code to crate a circular linked list of n nodes
    head = None
    for num in range(5):
        head = Node(num, head)
    
    tail = head
    probe = head
    while probe.next != None:
        probe = probe.next

    probe.next = tail

    probe = head
    index = 15
    while probe != None and index > 0:
        print(probe.data)
        probe = probe.next 
        index -= 1





if __name__ == "__main__":
        run()