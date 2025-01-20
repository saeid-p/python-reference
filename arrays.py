a1 = [1, 2, 3, 3, 4]

for item in a1:
    print(item)

# Return the number of times and element appears in an array:
occurrence = a1.count(3)  # 2

a1.append(5)  # Add element to end of array.
a1.insert(0, 10)  # Insert element 10 at index 0.

a2 = [6, 7, 8]
a1.extend(a2)  # Add elements of a2 to end of a1.

targetIndex = a2.index(6)  # Find element's index.
a2.pop(targetIndex)  # Removes by index
a2.remove(8)  # Remove by instance
a2.pop()  # Remove last element.

a2.reverse()

a2.sort()  # Sort in ascending order (Inplace)
a2.sort(reverse=True)  # Sort in descending order (Inplace)

# Sort a2 in ascending order using lambda
a2.sort(key=lambda x: x)

# Sort a2 in descending order using lambda
a2.sort(key=lambda x: -x)
