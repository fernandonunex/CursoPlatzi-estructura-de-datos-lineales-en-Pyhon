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
circular.append(5)
circular.size()
circular.append(2)
circular.append(2)
circular.append(2)
circular.size()

print(circular.tail.next.data)

