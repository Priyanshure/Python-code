# Creating a list with 25 integer values
numbers = [5, 9, 12, 7, 15, 22, 30, 41, 18, 33, 25, 44, 21, 36, 48, 55, 63, 70, 90, 99, 42, 14, 27, 11, 39]

# Loop through the list
for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is not divisible by 3")
