N=int(input("enter a no"))
if N<=10:
    print("Too cold! Best to stay indoors")
elif N>=20 and N<=30:
    print("Perfect for a picnic")
elif N>=10 and N<=19:
    print("Maybe wear a jacket")
else:
    print("It's hot. Let's go swimming!")