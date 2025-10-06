# List method examples in Python

fruits = ["apple", "banana", "cherry"]

# append() - add an item to the end
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# insert() - add an item at a specific position
fruits.insert(1, "grape")
print(fruits)  # ['apple', 'grape', 'banana', 'cherry', 'orange']

# remove() - remove first occurrence of a value
fruits.remove("banana")
print(fruits)  # ['apple', 'grape', 'cherry', 'orange']

# pop() - remove and return item at given index (default last)
last = fruits.pop()
print(last)    # orange
print(fruits)  # ['apple', 'grape', 'cherry']

# index() - get the index of a value
print(fruits.index("cherry"))  # 2

# count() - count occurrences of a value
print(fruits.count("apple"))   # 1

# sort() - sort the list
fruits.sort()
print(fruits)  # ['apple', 'cherry', 'grape']

# reverse() - reverse the list
fruits.reverse()
print(fruits)  # ['grape', 'cherry', 'apple']

# clear() - remove all items
fruits.clear()
print(fruits)  # []