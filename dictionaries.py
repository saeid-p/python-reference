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