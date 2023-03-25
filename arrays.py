from array import *

"""
In the array initializer, "Type code" represents signed integer of size 1 byte:
    B Represents unsigned integer of size 1 byte
    c Represents character of size 1 byte
    u Represents unicode character of size 2 bytes
    h Represents signed integer of size 2 bytes
    H Represents unsigned integer of size 2 bytes
    i Represents signed integer of size 2 bytes
    I Represents unsigned integer of size 2 bytes
    w Represents unicode character of size 4 bytes
    l Represents signed integer of size 4 bytes
    L Represents unsigned integer of size 4 bytes
    f Represents floating point of size 4 bytes
    d Represents floating point of size 8 bytes
"""

a1 = array('i', [1,2,3,4])

for item in a1:
    print(item)
    
a1.append(5)
a1.insert(0,0)

a2 = array('i', [6,7,8])
a1.extend(a1)

targetIndex = a2.index(6) # Find element's index.

a2.remove(8) # Remove by instance
a2.pop(len(a2) - 1) # Removes by index
a2.pop() # Remove last element.

a2.reverse()

# Return the number of times and element appears in an array:
a3 = [1,2,3,3,3,3]
print(a3.count(3)) # 4