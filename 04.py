# Creating a list with multiple data types
my_list = [10, 3.14, "Hello", True, [1, 2, 3], (4, 5, 6), {7, 8, 9}, {"key": "value"}, None, complex(2, 3)]

# Looping through the list and printing each element with its data type
for element in my_list:
    print(f"Element: {element}, Type: {type(element)}")
