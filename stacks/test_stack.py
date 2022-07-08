
from stack import Stack

food = Stack()

food.push('queso')
food.push('rompope')
food.push('torta')
food.push('panqueque')
food.push('red bull')

print(food.peek())
print("*"*20)
for foods in food.iter():
    print(foods)

print("*"*20)
print(food.peek())
print(food.search('red bull'))

food.clear_v2()
print("*"*20)
print(food.peek())
print(food.search('red bull'))
