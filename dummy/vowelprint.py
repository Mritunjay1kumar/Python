s=input("enter the string:")
r=""
v="AEIOUaeiou"
for p in s:
    if p in v:
        r=r+p
print(r)        
