array1=[1,2,3,4,5,6]
array2=[1,3,5,8,7,9]
i=0
a=[]
while i<len(array1):
    if array1[i]in array2:
        a.append(a[i])
    i+=1
print(a)