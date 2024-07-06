x=[]
n=int(input('enter n:'))
for i in range(n):
    no=int(input('enter no:'))
    x.append(no)
print("display even number")
for p in x:
    if p%2==0:
        print(p)
