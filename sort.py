# Input
numbers = input("Enter three numbers separated by space: ")
a, b, c = map(int, numbers.split())

# Sorting without using any function or method
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Output
print("Sorted numbers:", a, b, c)
