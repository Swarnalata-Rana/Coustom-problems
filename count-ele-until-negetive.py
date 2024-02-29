l = [10, 5, 6, 3, -1, 4, -3, 5, 6]
i = 0
c=0
while i < len(l):
    if l[i]<0:
        c+=i
        break
    i+=1
print(c)