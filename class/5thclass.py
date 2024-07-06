#enter 10 employ detail and display them
class emp:
    def accept(self):
        self.eid=int(input("enter emp id:"))
        self.ename=input("enter ename:")
        self.sal=float(input("enter salary:"))
    def display(self):
        print(self.eid," ",self.ename," ", self.sal)
x=[]
for i in range(10):
    e=emp()
    e.accept()
    x.append(e)
for i in range(10):
    x[i].display()
