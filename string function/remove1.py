n=int(input("enter n:"))
x=[]
for i in range(n):
    no=int(input("enter no:"))
    x.append(no)
i=0
while (i<len(x)-1):
    if x[i]<x[i+1]:
        x.remove(x[i])
    else:
        i+=1
print(x)        
