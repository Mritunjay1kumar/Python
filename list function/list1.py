x=[10,20,60]
print(len(x))
print(x)
x.append(45)
x.append(70)
print(x)
y=[20,90,70,40]
x.extend(y)
print(x)
x.append(20)
print(x)
a=x.count(20)
print(a)
a=x.count(75)
print(a)
p=x.index(20)
print('postion=',p)
#p=x.index(75)
#print('postion=',p)
y=x.copy()
print(y)
x.remove(20)
print(x)
no=x.pop()
print(no)
print(x)