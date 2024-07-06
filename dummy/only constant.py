import re
s=input("enter the string:")
for p in s:
    if p not in re.findall(r'[aeiouAEIOU]',s):
        print(p,end='')
    

