# Sets are unordered collection of unique values. Items must be hashable.

s1 = {1,2,'a'}

s1.add(3)
s1.remove('a')

print(s1) # {1,2,3}

print(s1.pop()) # Remove an arbitrary element from the set.


l1 = [1,2,3]
s2 = set(l1)
print(s2) # {1,2,3}

if 1 in s2:
    print('Found!')
    
# You can iterate like a list, but the values will be in an arbitrary order.
for item in s2:
    print(item)
    
# Frozen sets are immutable and new elements cannot added after its defined.
fs2 = frozenset(s2)
print(fs2)