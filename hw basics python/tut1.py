m1=int(input("enter the marks1:"))
m2=int(input("enter the marks2:"))
m3=int(input("enter the marks3:"))
total=m1+m2+m3
per=(total*100)/300
print("total:",total)
print("percentage:",per)
if per>=90:
    print("distinction")
elif per>=80:
    print("first class")
elif per>=70:
    print("second class")
elif per>=60:
    print("third class")
else:
    print("not eligible")
