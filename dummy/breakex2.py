no=int(input("enter the no:"))
i=1
while i<=no:
    if i%5==0:
        break
    print(i)
    i+=1
else:
    print("else block call duee to while")
print("finish due to break")    
