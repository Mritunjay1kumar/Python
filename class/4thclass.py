class student:
    def accept(self):
        self.rno=int(input("enter roll no:"))
        self.sname=input("enter name:")
        self.per=float(input("enter percentage"))
    def display(self):
        print(self.rno,' ',self.sname," ",self.per)
x=student()
y=student()
x.accept()
x.display()
