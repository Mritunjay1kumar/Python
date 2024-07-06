no=int(input("enter the no:"))
sum=0
temp=no
while no!=0:
    d=no%10
    no=no//10
    sum=sum*10+d
print("reverse of no:",sum)
if sum==temp:
    print("no is palindrome")
else:
    print("no is not palindrome")

