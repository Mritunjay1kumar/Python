''' create 2 base class  student(rno,sname,course) and 
     Marks(m1,m2,m3)  , create  derived class Result(total ,per) from studnet,marks class
   enter n student detials and display them '''

class Student:
     def acceptstudent(self):
               self.rno = int(input("enter roll no"))
               self.sname = input("enter name")
               self.course = input("enter course")
     def displaystudent(self):
          print(self.rno,"  ",self.sname,"  ",self.course,end="  ")

class Marks:
     def acceptmarks(self):
          self.m1 = int(input("enter m1"))
          self.m2 = int(input("enter m2"))
          self.m3 = int(input("enter m3"))
     
     def displaymarks(self):
          print(self.m1,"  ",self.m2," ",self.m3,"   ",end="  ")

class Result(Student,Marks):
     def acceptresult(self):
          self.acceptstudent()
          self.acceptmarks()
     def calculate(self):
          self.total = self.m1+self.m2+self.m3
          self.per = self.total / 3     
     def displayresult(self):
           self.displaystudent()
           self.displaymarks()
           print(self.total,"  ",self.per)

n = int(input("enter n"))      
x = []

for i in range(n):
     s = Result()
     s.acceptresult()
     s.calculate()
     x.append(s)

for p in x:
     p.displayresult()

print("Display student whose percentage > 60")

for p in x:
     if p.per >= 60:
          p.displayresult()

           
