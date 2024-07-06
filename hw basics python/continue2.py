no=int(input("enter the no:"))
for i in range(1,no):
    if i%3==0 or i%4==0:
        continue
    print(i)
print("finish the for loop")    
