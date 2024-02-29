array = [10, 5, 6, 3,4, 3, 5, 6]
i=0
min=array[0]
while i <len (array):
    if array[i]<min:
        min=array[i]
    i+=1
print("minmum element:-",min)