import re
s=input('enter string:')
p=re.match(r'java',s)
if p:
    print(p.group())
else:
    print('not match')
