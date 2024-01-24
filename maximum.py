numbers = input("Enter three numbers separated by space: ")
a, b, c = map(int, numbers.split())
max_number = a
if b > max_number:
    max_number = b
if c > max_number:
    max_number = c
print("The maximum number is:", max_number)
