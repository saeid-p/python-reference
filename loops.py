
i = 0
while i < 7:
    print(i)
    if i == 4:
        break
    i += 1
    
for i in range(0,4):    
    if i % 2:
        continue
    print(i)
    
for x in ['one', 'two', 'three', 'four']:
    print(x)

for i in range(3):
    if type(i) is not int:
        print(i)
        break
# The else clause only executes after a for loop terminates by iterating to completion, 
# or after a while loop terminates by its conditional expression becoming false.
# It does not execute if the loop terminates some other way:
    # Through a break statement or by raising an exception.
else:
    print('All good!')