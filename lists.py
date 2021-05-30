# List is an ordered collection of n values.
# Lists are not hashable nad they are mutable.

l1 = [1, 2, [3, 4, 5], 6, 7]
l2 = l1[2]

l1[2][0] = 30
print(l2[0]) # 30

l2[1] = 40
print(l1[2][1]) # 40