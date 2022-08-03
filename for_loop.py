nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item: int
print("List number: ")
for item in nums:
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