import os

if os.path.exists("test/demo/Employee.java"):
     print(os.path.abspath("test/demo/Employee.java"))
     print(os.path.basename("test/demo/Employee.java"))
     print(os.path.dirname("test/demo/Employee.java"))
     print(os.path.getsize("test/demo/Employee.java"))
else:
     print("File not found")
