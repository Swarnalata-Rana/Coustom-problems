array=[4, 7, 9 ,10 ,7, 14, 12, 4, 7 ,27]
i=0
c=0
while i<len(array):
    if array[i]==7:
       c+=1
    i+=1
print(c)