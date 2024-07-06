#enter string copy only alpha to another string
s=input('enter the string:')
r=''
for p in s:
    if p.isalpha():
        r=r+p
print(r)        
