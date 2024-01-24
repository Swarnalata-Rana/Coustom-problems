# l=[11, 1 ,13 ,21,3, 7]
# i=0
# while i<len(l):
#     if l>0:   
#         print("YES")
#     else:
#         print("NO")
#     i+=1
     


l = [11, 1, 13, 21, 3, 7]
i = 0
found_negative = False

while i < len(l):
    if l[i] < 0:
        found_negative = True
        break
    i += 1

if found_negative:
    print("NO")
else:
    print("YES")

    