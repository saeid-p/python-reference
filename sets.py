# Sets are unordered collection of unique values. Items must be hashable.

s1 = {1,2,'a'}

2 in s1 # True
4 not in {1,2,3} # True

s1.add(3)
s1.remove('a')
s1.discard(50) # Safe remove an element.

print(s1) # {1,2,3}

print(s1.pop()) # Remove an arbitrary element from the set.

l1 = [1,2,3,3]
s2 = set(l1)
print(s2) # {1,2,3}

if 1 in s2:
    print('Found!')
    
# You can iterate like a list, but the values will be in an arbitrary order.
for item in s2:
    print(item)
    
# Frozen sets are immutable and new elements cannot added after its defined.
fs2 = frozenset(s2)

# Intersection
s3 = {1, 2, 3, 4, 5}
s4 = {3, 4, 5, 6}
s3.intersection(s4) # {3, 4, 5}
s3 & s4 # {3, 4, 5}
# In-Place: &=

# Union
s3.union(s4) # {1, 2, 3, 4, 5, 6}
s3 | s4 # {1, 2, 3, 4, 5, 6}
# In-Place: |=

# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
{1, 2, 3, 4} - {2, 3, 5} # {1, 4}
# In-Place: -=

# Symmetric difference returns a new set with elements present in either a or b but not in both.
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5} # {1, 4, 5}
# In-Place: ^=

# Superset check
{1, 2}.issuperset({1, 2, 3}) # False
{1, 2} >= {1, 2, 3} # False

# Subset check
{1, 2}.issubset({1, 2, 3}) # True
{1, 2} <= {1, 2, 3} # True

# Disjoint check
{1, 2}.isdisjoint({3, 4}) # True
{1, 2}.isdisjoint({1, 4}) # False