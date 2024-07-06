import re
email=input("enter the email:")
p=re.match(r'[A-Za-z0-9]+_?\.?[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]+\.?[a-z]+',email)
if p:
    print("valid email=",p.group())
else:
    print("invalid email")
