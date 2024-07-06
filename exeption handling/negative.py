class NegativeException(Exception):
    pass
no=int(input('enter nu:'))
if no<0:
    raise NegativeException()
else:
    if no%2==0:
        print(no,"is even")
    else:
        print(no,"is odd")
#NegativeException        
