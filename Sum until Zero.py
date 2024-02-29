array=[10, 5, 6, 3, 0, 4, 3, 5, 6]
i=0
s=0
while i<len(array):
    if array[i]>0:
        s=s+array[i]
    else:
        break
    i+=1
print(s)
