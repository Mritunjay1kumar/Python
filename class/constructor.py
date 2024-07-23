class Calculator:
    num=100
    #default constructor
    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNum=b
        print('print I am in consturcotr')
    def getData(self):
        num=102
        print(f'Number is : {num}')
    def add(self):
        #print(a+b)
        return self.firstNumber+self.secondNum

obj=Calculator(2,3)
obj.getData()
print(obj.add())