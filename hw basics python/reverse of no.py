no=int(input("enter the no:"))
sum=0
while no!=0:
    d=no%10
    no=no//10
    sum=sum*10+d
print("reverse of no:",sum)   
