N=input("enter charecter")
S='abcdefgh'
i=0
while i<len(S):
    if i in S[i]:
        print("Yes")
    else:
        print("No")
    i+=1
