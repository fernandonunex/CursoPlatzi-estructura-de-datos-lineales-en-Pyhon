"""Code used to create the methods and testing the methods"""

from linked_list import SinglyLinkedList
from node import Node
from array_ import Array

# head = None
# for count in range(1,8): #Crear una serie de nodos de forma iterativa
#     head = Node(count, head)

#************************************************************************************
# 1. Recorrer una linked list
# probe = head
# while probe != None:
#     print(probe.data)
#     probe = probe.next

#************************************************************************************
# 2. Search a element in the linked list
# probe = head
# target_item = 2

# while probe != None and target_item != probe.data:
#     probe = probe.next

# if probe != None:
#     print(f"Target item {target_item} has been found")
# else:
#     print(f"Target item {target_item} is not in the linked list")

#************************************************************************************
# 3. Replace an element
# probe = head
# target_item = 1
# new_item = 'Z'

# while probe != None and target_item != probe.data:
#     probe = probe.next

# if probe != None:
#     probe.data = new_item
#     print(f"{new_item} replaced the old value in the node number {target_item}")
# else:
#     print(f"The target item {target_item} is not in the linked list")

#************************************************************************************
# 4. Insert a new element at the head
# new_node = Node('K')

# if head is None:
#     head = new_node
# else:
#     probe = head
#     while probe.next != None:
#         probe = probe.next
#     probe.next = new_node


#************************************************************************************
# 5. Remove item
# removed_item = head.data
# head = head.next
# print(f"-->{removed_item}")



#************************************************************************************
# 6. Remove item at the head
# removed_item = head.data
# if head.next is None:
#     head = None
# else:
#     probe = head
#     while probe.next.next != None:
#         probe = probe.next
#     removed_item = probe.next.data
#     probe.next = None

# print(f"--> {removed_item}")
    
#************************************************************************************
# 7. Insert an item in a specific position
# new_item = input("Enter new item: ")
# index = int(input("Enter the position to insert the new item: "))
# if head is None or index <= 0:
#     head = Node(new_item, head)
# else:
#     probe = head
#     while index > 1 and probe.next != None:
#         probe = probe.next
#         index -= 1
#     probe.next = Node(new_item, probe.next)

# probe = head
# while probe != None:
#     print(probe.data)
#     probe = probe.next

# print("--"*20)
#************************************************************************************
# 8. Delete a node from a position
# index = 3
# if index <= 0 or head.next is None:
#     removed_item = head.data
#     head = head.next
#     print(removed_item)
# else:
#     probe = head
#     while index > 1 and probe.next.next != None:
#         probe = probe.next
#         index -= 1
#     removed_item = probe.next.data
#     probe.next = probe.next.next
#     print(removed_item)

# print("--"*20)

# probe = head
# while probe != None:
#     print(probe.data)
#     probe = probe.next



print("Creating an Array with random numbers")
random = Array(10)
random.__fillRandom__()
print(random)
print("Creating a Linked list from an Array")
linked_random = SinglyLinkedList()
linked_random.array_to_linked(random)
linked_random.show_linked_list()
# linked_random.search(5)
# linked_random.replace_item(2,'dope')
# linked_random.show_linked_list()
print("***"*10)
# linked_random.insert_at_head('Yo soy la cabeza')
# linked_random.insert_in_index('I am the first',0)
# linked_random.insert_in_index('I am the second',1)
# linked_random.insert_in_index('I am the last one',20)
linked_random.delete_from_index(5)
linked_random.show_linked_list()
print("***"*10)
# linked_random.remove_the_head()
# linked_random.show_linked_list()



