nums = [1, 2, 3, 4, 5]
item: int
print("List odd number: ")
for item in nums:
    if item % 2 != 0:
        print(item)

#numbers = range(10)
#numbers = range(5, 10)
numbers = range(5, 10, 2)
print("Range number: ")
for number in numbers:
    print(number)
print("Even number: ")
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
    print(number)
print(f"We have {count} even numbers")

num = 1
print("Printing message: ")
for num in range(1, 10, 2):
    print("Attempt", num, num * "*")

successful = False
for num in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

for x in range(5):
    for y in range(3):
        print(f"[{y}, {x}]")

print(type(5))
print(type(range(5)))

# Iterable
#for x in "MySQL":
    #print(x)

for x in range(1, 15, 3):
    print(x)


names = ["John", "Tom", "Mike", "Amy", "Susana"]
#names.append("Sam")
#names.insert(0, "Sam")
#names.remove("Amy")
#names.clear()
#names.reverse()
print("The name in the list: ")
#items = [0, "John"]
#items = (0, "John")
#index, name = items

for index, name in enumerate(names):
    print(index, name)

print("Done")