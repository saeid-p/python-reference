# Variable names are case sensitive and can start with _
_variable1 = 'My Special Variable.'

# Get type of variable with type()
variableType = type(_variable1)
print(variableType)

num1 = 5 # typeof(num1) = <type 'int'>
num2 = 3.14 # typeof(num2) = <type 'float'>

str1 = 'String Value 1' # typeof(str1) = <type 'str'>
str2 = "A"

bool1 = True # typeof(bool1) = <type 'bool'>
bool2 = False

nullValue = None # Null values are defined as 'None'
print(nullValue) # Output: None, typeof(nullValue) = <class 'NoneType'>

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