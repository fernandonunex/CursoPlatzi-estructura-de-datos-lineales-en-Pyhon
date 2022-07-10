from list_based_queue import ListQueue

food = ListQueue()
food.enqueue('taco')
food.enqueue('arroz con leche')
food.enqueue('ice')
print(food.dequeue())
print(food.dequeue())
print(food.dequeue())

print("--"*10)
#food.traverse()



