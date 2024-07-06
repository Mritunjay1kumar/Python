class InvalidNameException(Exception):
    pass
name=input("enter name:")
if name.isalpha():
    print("name",name)
else:
    raise InvalidNameException()
#InvalidNameException
