x=[10,5,3,4,3,5,6]
i=0
a=[]
while i<len(x):
    if x[i]in a:
        if x[i]==a[i]:
            a.append(x[i])
        i+=1
print(a)

