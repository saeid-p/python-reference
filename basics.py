# Get user input from console.
userInput = input('Provide some values: ')
print('User input: \'{}\''.format(userInput))

# Variable names are case sensitive and can start with _
_variable1 = 'My Special Variable.'

# Get type of variable with type()
variableType = type(_variable1)
print('variableType', variableType)

# Integers in Python are of arbitrary sizes.
num1 = 5 # typeof(num1) = <type 'int'>

# For floating point number; precision depends on the implementation and system architecture:
    # For CPython, the float datatype corresponds to a C double.
num2 = 3.14 # typeof(num2) = <type 'float'>

# complex: Complex numbers
c1 = 2 + 1j
c2 = 100 + 10j

str1 = 'hello' # typeof(str1) = <type 'str'>
print('Is str?', isinstance(str1, str)) # True

# With one letter labels in front of the quotes, you can tell what type of string you want to define.
'foo \n bar' # results str. The escaped character will be considered.
r'foo \n bar' # Raw string, where escaping special characters is not necessary.
b'foo bar' # bytes in Python 3, str in Python 2
u'foo bar' # str in Python 3, unicode in Python 2

bool1 = True # typeof(bool1) = <type 'bool'>
bool2 = False
print(issubclass(type(bool1), bool)) # True
print(issubclass(bool, int)) # True

# None doesn't have any natural ordering.
# Using ordering comparison operators (<, <=, >=, >) isn't supported anymore and will raise a TypeError.
nullValue = None # Null values are defined as 'None'
print('nullValue', nullValue) # Output: None, typeof(nullValue) = <class 'NoneType'>
print('Value is None', nullValue is None) # True
print('Value is not None', nullValue is not None) # False

# You can have multiple assignments. If the count of two sides don't match, and error will be thrown.
a, b, c = 1,2,3
x = y = z = 1

# Reference types like lists and dictionaries are acting accordingly.
l1 = l2 = [1,2,3]
l1[0] = 5
print(l2[0]) # 5

l3 = l4 = [1,2,3]
l3 = [4,5,6]
print(l4[0]) # 1

# Variables in Python do not have to stay the same type as which they were first defined.
# You can simply assign them to a new value even if that value is of a different type.

# Python uses the colon symbol (:) and indentation for showing where blocks of code begin and end.
if a > b:
    print(a)
    print(b)
elif a < b:
    print(b)
    print(a)
else:
    print(a,b) 

# You can simplify decisions this way:
if a > b: print(a)
else: print(b)

if x and y:
    print(x)

if x or y:
    print(y)

# Type Casting:
val1 = '123'
val2 = int(val1)
val3 = float('12.35')

list(str1) # ['h', 'e', 'l', 'l', 'o']
set(str1) # {'o', 'e', 'l', 'h'}
tuple(str1) # ('h', 'e', 'l', 'l', 'o')

# An object is hashable if it has a hash value which never changes during its lifetime
# It needs a __hash__() method, and can be compared to other objects (it needs an __eq__() method).
# Hashable objects which compare equality must have the same hash value.