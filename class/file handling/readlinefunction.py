import os

if os.path.exists("sample.txt"):
     fr =  open("sample.txt","r")
     s = fr.readline()
     print(s)
     s = fr.readline()
     print(s)
else:
     print("file not found")
