class emp:
    def set(self,a,b,c):
        self.eid=a
        self.ename=b
        self.sal=c
    def show(self):
        print(self.eid, " ",self.ename, " ",self.sal)
x=emp()
y=emp()
z=emp()
x.set(101,'ravi',4500)
x.show()
y.set(102,"ram",4600)
y.show()
z.set(103,'mohan',4700)
z.show()
