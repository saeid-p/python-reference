# List is an zero-indexed ordered collection of n values.
# Lists are not hashable and they are mutable. Therefore, they serve as a dynamic array.
# The elements of a list are not restricted to a single data type.

l1 = [1, 2, [3, 4, 5], 6, 7]
l2 = l1[2]

# Indices can also be negative which means counting from the end of the list.
# -1 being the index of the last element).

l1[2][0] = 30
print(l2[0]) # 30

l2[1] = 40
print(l1[2][1]) # 40

l3 = []
l3.append(2)
l3.append(3)
l3.append(4)
l3.append(4)
l3.insert(0, 1)
# l3 = [1,2,3,4,4]

lenOfList = len(l3) # 5
occurrences = l3.count(4) # 2
indexOfTarget = l3.index(2) # 1

l3.remove(2) # Removes the first occurrence of the provided value in the list.
l3.reverse() # Reverses the list.
l3[::-1] # Another way to reverse a list.

l3.pop(3) # Remove and return item at index (defaults to the last item).

# Iteration:
for item in l3:
    print(item)