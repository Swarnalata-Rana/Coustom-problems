n=int(input("enter any num="))
f=0
i=1
while i<n:
	if n%i==0:
		f=f+i
	i=i+1
if f==n:
	print(n,"perfect number")
else:
	print(n,"not a perfect number")



    