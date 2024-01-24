N = int(input("Enter a number: "))
s = 0
while N > 0:
    num = N % 10
    N=N//10
    s=s+num
print("Sum of Number:", s)
