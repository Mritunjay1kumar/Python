import os

if os.path.exists("sample.txt"):
     fr = open("sample.txt","r")
     fc = open("cap.txt","w")
     fs = open("small.txt","w")
     fd = open("digit.txt","w")
     fo = open("other.txt","w")
     s = fr.read()

     for p in s:
          if p.isupper():
               fc.write(p)
          elif p.islower():
               fs.write(p)
          elif p.isdigit():
               fd.write(p)
          else:
               fo.write(p)
               
     fr.close()
     fs.close()
     fc.close()
     fd.close()
     fo.close()
     
else:
     print("file not found")
