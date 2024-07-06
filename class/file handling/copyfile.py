import os

if os.path.exists("sample.txt"):
     fr = open("sample.txt","r")
     fw = open("test.txt","w")
     s = fr.read()
     fw.write(s)
     
     fr.close()
     fw.close()
else:
     print("file not found")
