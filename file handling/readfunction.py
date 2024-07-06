import os
if os.path.exists("sample.txt"):
    fr=open("sample.txt","r")
    p=fr.read()
    fw=open("test.txt","w")
    fw.write(p)
else:
    print("file not find")
    
    
