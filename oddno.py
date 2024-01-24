N = int(input("Enter a number: "))
i = 1
count = 0
while count < N:
    if i % 2 != 0:
        print(i)
        count += 1
    i += 1