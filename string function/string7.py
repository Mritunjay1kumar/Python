s=input("enter the string")
for p in s:
    if not p.isalnum():
        print(p,end="")

