N=int(input("enter a no"))
if N>=0 and N<=2:
    print("Infant")
elif N>=3 and N<=12:
    print("Child")
elif N>=13 and N<=19:
    print("Teenager")
elif N>=20 and N<=65:
    print("Audlt")
else:
    print("Senior")