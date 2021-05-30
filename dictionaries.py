# Dictionaries are unordered collection of unique key-value pairs; keys must be hashable.
d1 = {
    1: 'one',
    2: 'two'
 }

print(d1[1]) # one

d1[3] = 'three'
print(d1[3]) # three

d1.pop(3)
print(d1) # {1: 'one', 2: 'two'}

d2 = {
    'a': [1, 2, 3],
    'b': 'String Value'
}

for key in d2.keys():
    print('Key: \'{}\' - Value: \'{}\''.format(key, d2[key]))

for key, value in d2.items():
    print(key, "::", value)

#### Safe Search ####
item  = d2.get('c', 'default')

if 'd' in d2:
    value = d2['d']

#### defaultdict ####
# A defaultdict is a dictionary with a default value for keys.
# Keys for which no value has been explicitly defined can be accessed without errors.
from collections import defaultdict

dd1 = defaultdict(lambda: -1)
dd1[1] = 5

print('dd1[1]', dd1[1]) # 5
print('dd1[2]', dd1[2]) # -1

#### Ordered Dictionary ####
from collections import OrderedDict
od1 = OrderedDict()
od1['first'] = 1
od1['second'] = 2
od1['third'] = 3
od1['last'] = 4