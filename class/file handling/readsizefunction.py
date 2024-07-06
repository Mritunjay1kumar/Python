import os

if os.path.exists("sample.txt"):
     fr =  open("sample.txt","r")
     s = fr.read(6)
     print(s)
else:
     print("file not found")
