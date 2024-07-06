import re
s="ejava is oops language"
p=re.split(r"[aeiou]",s)
print(p)
q=re.findall(r"[aeiou]",s)
print(q)
