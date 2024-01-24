N = int(input("Enter a number: "))
c = 0
while N > 0:
    N=N//10
    c += 1
print("Counting of digits:", c)