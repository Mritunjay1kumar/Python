class demo:
    a=12
    def one(self):
        print("hello")
class test(demo):
    b=7.6
    c=34
    def two(self):
        print("vb")
x=test()
print(x.b)
print(x.c)
x.two()    
