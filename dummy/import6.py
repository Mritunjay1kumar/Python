import re
s=input("enter the string:")
p=re.findall(r"[aeiouAEIOU]",s)
m=''.join(p)
print(m)
