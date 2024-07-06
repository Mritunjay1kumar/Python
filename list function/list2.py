x=[]
n=int(input('enter n:'))
for i range(n):
    no=int(input("enter no:"))
    x.append(no)
for p in x:
    t=p
    while p!=0:
        d=p%10
        p=p//10
        if d%2==0:
            print(t)
