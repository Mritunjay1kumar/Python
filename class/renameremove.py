import os

if os.path.exists("Employee.java"):
     os.rename("Employee.java","Student.java")
     os.remove("First.java")
else:
     print("file not found")
