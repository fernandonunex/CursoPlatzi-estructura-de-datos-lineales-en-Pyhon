from stack import Stack_list


books = Stack_list(5)
# Cheking the init
print("**"*10)
print(books._size)
print(books._counter)

#Testing the iter when is empty
print("**"*10)
for book in books.iter():
    print(book)

# Testing the push method
print("**"*10)
books.push('The lean Startup')
books.push('La incubacion')
books.push('Why we sleep')
books.push('Scrum')
books.push('La ciudad de las bestias')
# print(books.push('Caperusita'))
print(books._counter)
print("**"*10)

# Testing the iter with some books
for book in books.iter():
    print(book)

print("**"*10)
# Testing the pop method
# print(f"peek -> {books.pop()}")
# print(f"peek -> {books.pop()}")
# print(f"peek -> {books.pop()}")

#Testing the search method

index = books.search('The lean gStartup')
print(index)


print("**"*10)
# Testing the iter with some books
for book in books.iter():
    print(book)

# Testing the method clear
books.clear()
print("**"*10)

for book in books.iter():
    print(book)