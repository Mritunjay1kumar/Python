''' create a base class  student(rno,sname,course) , create another derived class
     Marks(m1,m2,m3,total,per) from student class
   enter n student detials and display them '''


class Studnet:
     def acceptstudent(self):
               self.rno = int(input("enter roll no"))
               self.sname = input("enter name")
               self.course = input("enter course")
     def displaystudent(self):
          
               print(self.rno,"  ",self.sname,"  ",self.course,end="  ")

class Marks(Studnet):
     def acceptmarks(self):
          self.acceptstudent()
          self.m1 = int(input("enter m1"))
          self.m2 = int(input("enter m2"))
          self.m3 = int(input("enter m3"))
     def calculate(self):
          self.total = self.m1+self.m2+self.m3
          self.per = self.total/3

     def displaymarks(self):
          
          self.displaystudent()
          
          print(self.m1,"  ",self.m2," ",self.m3,"   ",self.total,"  ",self.per)
          


n = int(input("enter n"))      
x = []

for i in range(n):
     s = Marks()
     s.acceptmarks()
     s.calculate()
     x.append(s)

for p in x:
     p.displaymarks()
