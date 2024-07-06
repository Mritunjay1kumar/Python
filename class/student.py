class Student:

          def accept(self):
               self.rno = int(input("enter roll no"))
               self.sname = input("enter name")
               self.course = input("enter course")
               self.m1 = int(input("enter m1"))
               self.m2 = int(input("enter m2"))
               self.m3 = int(input("enter m3"))
          def calculate(self):
               self.total = self.m1+self.m2+self.m3
               self.per = self.total/3
          def display(self):
               print(self.rno,"  ",self.sname,"  ",self.course,"  ",self.m1,"  ",self.m2," ",self.m3,"   ",self.total,"  ",self.per)

n = int(input("enter n"))      
x = []

for i in range(n):
     s = Student()
     s.accept()
     s.calculate()
     x.append(s)

for p in x:
     p.display()
               
               
               
