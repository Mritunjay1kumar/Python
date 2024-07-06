no=int(input("enter the no:"))
s=""
while no!=0:
    d=no%10
    no=no//10
    if d==0:
        s="zero"+s
    elif d==1:
        s="one "+s
    elif d==2:
        s="two "+s
    elif d==3:
        s="three "+s
    elif d==4:
        s="four "+s
    elif d==5:
        s="five "+s
    elif d==6:
        s="six "+s
    elif d==7:
        s="seven "+s
    elif d==8:
        s="eight "+s
    else:
        s="nine "+s
print(s)        
