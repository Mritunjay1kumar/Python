s=input("enter string:")
r=s.split(" ")
x=[]
for p in r:
    x.append(len(p))
print("max=",max(x))
