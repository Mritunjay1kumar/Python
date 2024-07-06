import re
email=input('enter email:')
p=re.Match(r'[A-Za-z0-9]+_?\.[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]+\.?[a-z]+',email)
if p:
    print("valid email=",email)
else:
    print("invalid email")
