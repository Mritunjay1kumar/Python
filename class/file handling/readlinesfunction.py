import os

if os.path.exists("sample.txt"):
     x =  open("sample.txt","r")
     s = x.readlines()
     print(s)
     
else:
     print("file not found")
