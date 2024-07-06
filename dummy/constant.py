s=input("enter the string:")
r=""
v="AEIOUaeiou"
for p in s:
    if p.isalpa()and p not in v:
        r=r+p
print("consonent",r)        
