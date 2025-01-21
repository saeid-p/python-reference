# Lambda functions are used to create anonymous functions.
# They are useful for creating quick functions without the need to define a full function.


# You can define a lambda function as a variable.
lambda_function = lambda x: x + 1


def test_function(x):
    return x + 1


items = [1, 2, 3, 4, 5]

# Map applies a function to all items in an iterable.
mapped_items = list(map(lambda x: x * 2, items))
mapped_items_with_predefined_lambda = list(map(lambda_function, items))
mapped_items_with_predefined_function = list(map(test_function, items))

print(mapped_items)  # [2, 4, 6, 8, 10]

# Filter applies a function to all items in an iterable and returns a new list with only the items that satisfy the function.
filtered_items = list(filter(lambda x: x % 2 == 0, items))

print(filtered_items)  # [2, 4]
