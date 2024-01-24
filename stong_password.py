x=input("enter your password:-")
if (x>="a" and x<="z") or (x>="A" and x<="Z") or (x<="0" and x>="9") or (x=="@",x=="#"):
 if len(x)>=8 and len(x)<=12:
    print("strong password")
 else:
    print("incorrect password")