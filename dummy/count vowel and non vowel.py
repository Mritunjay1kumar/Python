import re
s=input("enter the string:")
print(len(s))
count=0
for p in s:
    if p in re.findall(r'[aeiouAEIOU]',s):
        count=count+1
print(count)
print('non vowel is',len(s)-count)
        
