# List is an zero-indexed ordered collection of n values.
# Lists are not hashable and they are mutable. Therefore, they serve as a dynamic array.
# The elements of a list are not restricted to a single data type.

l1 = [1, 2, [3, 4, 5], 6, 7]
l2 = l1[2]

# Indices can also be negative which means counting from the end of the list.
# -1 being the index of the last element).

l1[2][0] = 30
print(l2[0])  # 30

l2[1] = 40
print(l1[2][1])  # 40

l3 = []
l3.append(2)
l3.append(3)
l3.append(4)
l3.append(4)
l3.insert(0, 1)
print("l3", l3)  # [1,2,3,4,4]

lenOfList = len(l3)  # 5
occurrences = l3.count(4)  # 2
indexOfTarget = l3.index(2)  # 1

l3.remove(2)  # Removes the first occurrence of the provided value in the list.
l3.reverse()  # Reverses the list.
l3[::-1]  # Another way to reverse a list.

l3.pop(3)  # Remove and return item at index (defaults to the last item).

lst = []
if not lst:
    print("List is empty!")

if 3 in l3:
    print("Found!")

# Iteration:
for item in l3:
    print("item", item)

l4 = [1, 2]
l5 = [3, 4]
mixedList = l4 + l5  # [1,2,3,4]

#### Slicing ####
"""
Lists allow to use slice notation as lst[start:end:step].
The output is a new list containing elements from index start to the end.
If options are omitted, start defaults to the beginning of list, and end to the end of list. Step defaults to 1.
"""

lst = [1, 2, 3, 4]
lst[1:]  # [2, 3, 4]
lst[:3]  # [1, 2, 3]
lst[::2]  # [1, 3]
lst[::-1]  # [4, 3, 2, 1]
lst[-1:0:-1]  # [4, 3, 2]
lst[5:8]  # [] since starting index is greater than length of lst, returns empty list
lst[1:10]  # [2, 3, 4] same as omitting ending index

#### List Comprehensions ####
# A list comprehension creates a new list by applying an expression to each element of an iterable.
squares = [x * x for x in (1, 2, 3, 4)]  # [1, 4, 9, 16]
[s.upper() for s in "Hello"]  # ['H','E','L','L','O']
[x if x in "accept" else "*" for x in "apple"]  # ['a', '*', '*', 'e', '*', '*']

# Conditional List Comprehension
# Template: [expression for item in iterable]
[x for x in range(10) if x % 2 == 0]
[x if x % 2 == 0 else None for x in range(10)]
[2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]

#### List Comparisons ####
[1, 10, 100] < [2, 10, 100]  # True, because 1 < 2
[1, 10, 100] < [1, 10, 100]  # False, because the lists are equal
[1, 10, 100] <= [1, 10, 100]  # True, because the lists are equal
[1, 10, 100] < [1, 10, 101]  # True, because 100 < 101
[1, 10, 100] < [0, 10, 100]  # False, because 0 < 1
# If one of the lists is contained at the start of the other, the shortest list wins.
