import os

if os.path.exists("sample.txt"):
     fr = open("sample.txt","r")
     cap=""
     sml=""
     dig=""
     ot=""
     s = fr.read()

     for p in s:
          if p.isupper():
               cap = cap+p
          elif p.islower():
               sml = sml+p
          elif p.isdigit():
               dig = dig+p
          else:
               ot = ot+p
               
     fr.close()
     print("capital letter = ",cap)
     print("small letter = ",sml)
     print("digits letter = ",dig)
     print("other symbol letter = ",ot)
     
     
else:
     print("file not found")
