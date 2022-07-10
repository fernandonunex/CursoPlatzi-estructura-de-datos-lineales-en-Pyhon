from list_based_queue import ListQueue
from stack_based_queue import Queue

# food = ListQueue()
# food.enqueue('taco')
# food.enqueue('arroz con leche')
# food.enqueue('ice')
# print(food.dequeue())
# print(food.dequeue())
# print(food.dequeue())

# print("--"*10)
#food.traverse()


# Testing stack based queue

# checando como se comportan ambos stacks
numbers = Queue()
numbers.enqueue(5)
numbers.enqueue(6)
numbers.enqueue(7)
numbers.enqueue(8)
print(numbers.inboud_stack)
print(numbers.outbound_stack)
print(numbers.dequeue())
print(numbers.inboud_stack)
print(numbers.outbound_stack)
numbers.enqueue(9)
numbers.enqueue(10)
print(numbers.inboud_stack)
print(numbers.outbound_stack)
print(numbers.dequeue())
print(numbers.inboud_stack)
print(numbers.outbound_stack)
print(numbers.dequeue())
print(numbers.inboud_stack)
print(numbers.outbound_stack)
print(numbers.dequeue())
print(numbers.inboud_stack)
print(numbers.outbound_stack)
print(numbers.dequeue())
print(numbers.inboud_stack)
print(numbers.outbound_stack)










