no=int(input("enter the no:"))
s=0
t=no
while no!=0:
    d=no%10
    no=no//10
    s=s*10+d
if s==t:
    print("no is reverse")
else:
    print("no is not reverse")
