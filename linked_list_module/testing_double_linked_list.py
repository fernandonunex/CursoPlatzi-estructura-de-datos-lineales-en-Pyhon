# from double_linked_list import Node, TwoWayNode
from circular_double_linked_list import CircleDoubleLinkedList

# head = TwoWayNode(1)
# tail = head
# for data in range(2,6):
#     tail.next = TwoWayNode(data, tail)
#     tail = tail.next

# probe = tail

# while probe != None:
#     print(probe.data)
#     probe = probe.previous

circular = CircleDoubleLinkedList()
circular.size()
circular.append('inicio')
circular.size()
circular.append(2)
circular.append(2)
circular.append('aloa')

print(f"size: {circular.size()}")

# print(circular.head.next.data)

# for data in circular.iter():
#     print(data)

# print("**"*10)
# for data in circular.reverse_iter():
#     print(data)

print("**"*10)
# pointer_of_data = circular._get_node_by_data('aloa')
# print(pointer_of_data.data)

# pointer_of_data = circular._get_node_by_index(0)
# print(pointer_of_data.data)
# pointer_of_data = circular._get_node_by_index(1)
# print(pointer_of_data.data)
# pointer_of_data = circular._get_node_by_index(2)
# print(pointer_of_data.data)
# pointer_of_data = circular._get_node_by_index(3)
# print(pointer_of_data.data)
# pointer_of_data = circular._get_node_by_index(4)
# print(pointer_of_data.data)
# pointer_of_data = circular._get_node_by_index(2)
# print(pointer_of_data.data)
# pointer_of_data = circular._get_node_by_index(5)
# print(pointer_of_data.data)
# pointer_of_data = circular._get_node_by_index(1)
# print(pointer_of_data.data)

circular.show_data()
print("**"*10)
circular.delete_node_by_data('inicio')
# print(circular.tail.data)
print("**"*10)
circular.show_data()
circular.delete_node_by_data(2)
circular.show_data()
circular.delete_node_by_data(2)
circular.show_data()
circular.delete_node_by_data('aloa')
circular.show_data()



