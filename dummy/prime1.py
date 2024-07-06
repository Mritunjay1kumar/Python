#x=int(input('enter num:'))
n=int(input('enter num:'))
for no in range(1,n):
    for i in range(2,no-1):
         if no%i==0:
        #print("not prime")
             break
else:
    print(no,end=" ")
