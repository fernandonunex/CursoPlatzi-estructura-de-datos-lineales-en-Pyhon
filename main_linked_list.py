from linked_list import SinglyLinkedList


if __name__ == "__main__":
    foods = SinglyLinkedList()
    foods.append('mole')
    foods.append('arroz')
    foods.append('enchiladas')

    for food in foods.iter():
        print(food)

    print("Deleting")
    print(foods.delete('enchiladas'))
