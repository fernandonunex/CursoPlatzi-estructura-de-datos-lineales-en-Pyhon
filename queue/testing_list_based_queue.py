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
# numbers = Queue()
# numbers.enqueue(5)
# numbers.enqueue(6)
# numbers.enqueue(7)
# numbers.enqueue(8)
# print(numbers.inboud_stack)
# print(numbers.outbound_stack)
# print(numbers.dequeue())
# print(numbers.inboud_stack)
# print(numbers.outbound_stack)
# numbers.enqueue(9)
# numbers.enqueue(10)
# print(numbers.inboud_stack)
# print(numbers.outbound_stack)
# print(numbers.dequeue())
# print(numbers.inboud_stack)
# print(numbers.outbound_stack)
# print(numbers.dequeue())
# print(numbers.inboud_stack)
# print(numbers.outbound_stack)
# print(numbers.dequeue())
# print(numbers.inboud_stack)
# print(numbers.outbound_stack)
# print(numbers.dequeue())
# print(numbers.inboud_stack)
# print(numbers.outbound_stack)


#TESTING QUEUES BASED IN NODES

# from node_base_queue import Queue_node

# food = Queue_node()
# food.enqueue('gorditas')
# food.enqueue('carne asada')
# food.enqueue('ensalada')

# print(food.head.next.data)
# print(food.tail.data)
# print(food.tail.previous.data)
# print(food.count)
# print(food.dequeue())
# print(food.head.data)


# TESTING PLAYLIST CLASS

from playlist import Playlist, MediaPlayerQueue, Track

# zoe_playlist = Playlist()
# flag = ''
# while flag != 'exit':
#     zoe_playlist.add_song()
#     flag = input("Enter 'exit' to stop adding songs or press 'Enter' to continue:")

# zoe_playlist.play()



# songs to just copy and paste in terminal:
# Poli Zoe 180
# No me destruyas Zoe 240
# Vía Láctea Zoe 240
# Reptilectric Zoe 230

# TESTING THE CODE OF PROFESSOR

track1 = Track("Highway to hell")
track2 = Track("Go!")
track3 = Track("Light years")
track4 = Track("Heartbreaker")
track5 = Track("Breath me") 
track6 = Track("How to dissappear completely")

media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2) 
media_player.add_track(track3) 
media_player.add_track(track4) 
media_player.add_track(track5) 
media_player.add_track(track6) 

media_player.play()



