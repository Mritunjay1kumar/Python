
x=int(input("enter the no x:"))
y=int(input("enter the no y:"))
s1=0
s2=0
for i in range(1,x):
    if x%i==0:
        s1=s1+i
print(s1)
for i in range(1,y):
    if y%i==0:
        s2=s2+i
print(s2)
if s1==y and s2==x:
    print("amicable")
else:
    print("not amicable")


