print("Hello world")
N=int(input("Enter NO"))
i=1
f=0
while i<=(N):
    if N%i==0:
        f+=1
    i+=1
if f==2:
    print("Prime Number")
else:
    print("Not Prime Number")