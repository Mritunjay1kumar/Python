m=input('enter the string')
c=" "
s=" "
d=" "
o=" "
for p in m:
    if p.isupper():
        c=c+p
    elif p.islower():
        s=s+p
    elif p.isdigit():
         d=d+p
    else:
        o=o+p
print('capital=',c)
print('small=',s)
print('digit=',d)
print('other=',o)
