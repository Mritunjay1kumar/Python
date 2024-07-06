class movie:
    def accept(self):
        self.mvno=int(input('enter mvno:'))
        self.mvname=input('enter mvname:')
        self.ryear=int(input('enter year:'))
    def display(self):
        print(self.mvno," ",self.mvname," ",self.ryear)
n=int(input('enter n:'))
x=[]
for i in range(n):
    m=movie()
    m.accept()
    x.append(m)
for p in x:
    p.display()
print('display movie which released after 2007')
for p in x:
    if p.ryear>2007:
        p.display()
