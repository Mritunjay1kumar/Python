class demo:
    def __init__(self):
        print("object create")
    def show(self):
        print("php")
    def __del__(self):
        print("object destroyed")
def one():
    x=demo()
    x.show()
y=demo()
one()
z=demo()
z.show()
