no=int(input("enter the no:"))
while no>0:
    print("twice of no is",2*no)
    if no%2==1 and no%4==3:
        break
    #finte loop due to no
else:
    print("i am due to full excution of while loop")
print("finish due to break ")    
