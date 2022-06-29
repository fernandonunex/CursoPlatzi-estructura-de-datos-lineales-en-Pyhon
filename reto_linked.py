from traceback import print_tb
from array_ import Array
from linked_list import SinglyLinkedList


def run():
    random_int = Array(5)
    random_int.__fillRandom__()
    print(random_int)
    
    random_int_linked = SinglyLinkedList()

    print("Creating the random_int_linked")
    for num in random_int.__iter__():
        random_int_linked.append(num)

    print("Printing all the created nodes in the linked list")
    for random in random_int_linked.iter():
        print(random)



if __name__ == "__main__":
        run()