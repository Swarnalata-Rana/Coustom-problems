N = int(input("Enter Number"))
i = 1
while i <= N:
    print((i * 2) + 1)
    i += 1
    # o/p-3 5 7 9 11 13 15



N = int(input("Enter Number"))
i = 0
while i < N:
    print((i * 3) + 2)
    i += 1
    # o/p-2 5 8 11 14 17 20

# /////
N = int(input("Enter Number"))
i = 3
count = 0
while count < N:
    print(i, end=' ')
    i *= 2
    count += 1
    # o/p-3 6 12 24 48 96 192

N = int(input("Enter Number: "))
i = 1
count = 0
sum_odd = 0

while count < N:
    if i % 2 != 0:
        print(i, end=' ')
        sum_odd += i
        count += 1
    i += 1
print("Odd sum:-" ,sum_odd)
# o/p-1 3 5 7 9 11 13 Odd sum:- 49