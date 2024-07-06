n=int(input("enter no:"))
for no in range(1,n):
    for i in range(2,no):
        if(no%i==0):
       #print(no,"is not prime")
            break 
        else:
            print(no,end=" ")
