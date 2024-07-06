import os

if os.path.exists("isfileisdir.py"):
     fr =  open("isfileisdir.py","r")
     s = fr.read()
     print(s)
else:
     print("file not found")
