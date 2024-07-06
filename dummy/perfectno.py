no=int(input("enter the no:"))
s=0
for i in range(1,no):
    if no%i==0:
        s=s+i
if s==no:
    print(no,'is pefect')
else:
    print(no,'is not perfect')
