#enter n student roll no and name save and display them
n=int(input("enter no of student:"))
x={ }
for i in range(n):
    rno=int(input("enter roll no:"))
    sname=input('enter name')
    x.update({rno:sname})
print(x)
