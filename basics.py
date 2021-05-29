# Variable names are case sensitive and can start with _
_variable1 = 'My Special Variable.'
print(_variable1)

# You can have multilple assignments. If the count of two sides don't match, and error will be thrown.
a, b, c = 1, 2, 3

x = y = z = 1

num1 = 5 # typeof(num1) = <type 'int'>
num2 = 3.14 # typeof(num2) = <type 'float'>

str1 = 'String Value 1' # typeof(str1) = <type 'str'>
str2 = "A"

bool1 = True # typeof(bool1) = <type 'bool'>
bool2 = False

# Get type of varilable with type()
bool2Type = type(bool2)
print(bool2Type)

nullValue = None # Null values are defined as 'None'
print(nullValue) # Output: None, typeof(nullValue) = <class 'NoneType'>