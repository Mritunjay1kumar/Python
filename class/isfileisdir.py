import os


if os.path.isfile("test/demo/Employee.java"):
     print("it is file")
else:
     print("it is not file")


if os.path.isdir("test/demo"):
     print("it is directory")
else:
     print("it is not directory")
