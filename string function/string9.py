s=input("enter the string:")
v="AEIOUaeiou"
for p in s:
    if p not in v:
        print(p)
