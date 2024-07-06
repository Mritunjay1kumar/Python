import re
s=input("enter the string:")
l=len(s)
for p in s:
    if p  in re.findall(r'[aeiouAEIOU]',s):
        print(p)
        
        
