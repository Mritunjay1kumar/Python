def sumofdigit(no):
    s=0
    while no!=0:
        d=no%10
        no=no//10
        s=s+d
    return s
no=int(input('enter no:'))
r=sumofdigit(no)
print(r)

