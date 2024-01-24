num=int(input("enter no:-"))
sum=0
a=num
while num>0:
	digit=(num%10)(num%10)(num%10)
	sum=sum+digit
	num=num//10
if a==sum:
	print('armstrong no')
else:
	print('not')
