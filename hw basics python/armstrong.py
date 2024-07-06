no=int(input("enter the no:"))
temp=no
sum=0
while no!=0:
    d=no%10
    no=no//10
    sum=sum+d**3
print("no is:",sum)
if sum==temp:
    print("no is armstong")
else:
    print("no is not armstong")
