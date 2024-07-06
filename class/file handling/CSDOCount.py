import os

if os.path.exists("sample.txt"):
     fr = open("sample.txt","r")
     cap=0
     sml=0
     dig=0
     ot=0
     s = fr.read()

     for p in s:
          if p.isupper():
               cap = cap+1
          elif p.islower():
               sml = sml+1
          elif p.isdigit():
               dig = dig+1
          else:
               ot = ot+1
               
     fr.close()
     print("capital = ",cap)
     print("small = ",sml)
     print("digits = ",dig)
     print("other symbol = ",ot)
     
     
else:
     print("file not found")
