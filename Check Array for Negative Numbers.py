
l = [11, 1, 13, 21, 3, -7,7]
i = 0
c=0
while i < len(l):
    if l[i] < 0:
        c+=1
        break
    i += 1
    
if c>0:
    print("Yes")
else:
    print("No")

    