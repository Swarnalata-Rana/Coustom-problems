array=[10 ,5 ,6 ,3 ,4 ,3 ,5 ,6]
i=0
max=0
while i<len(array):
    if array[i]>max:
        max=array[i]
        i+=1
print(max)