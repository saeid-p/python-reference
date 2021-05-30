# Tuples are ordered collection of n values of any type.
# Tuple supports indexing. It is immutable and hashable if all its members are hashable.
# Tuples are commonly used for small collections of values that will not need to change.

# Tuple classic syntax:
t0 = tuple(['Only member'])

t1 = (1,2,3)
t2 = ('a', 1, 'Test Phrase', (1,2), t1)

print(t2[2]) # 'Test Phrase'
print(t2[4]) # (1,2,3)

t3 = (1, 2)
print(t3 == t2[3]) # True