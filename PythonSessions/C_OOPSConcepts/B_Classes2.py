#Declaring the constructors in class
#Constructors are declared using: __inti__()
class MyClass:
    def m1(self):
        print("Good Morning")
    def __init__(self):
        print("this is from constructor")
c=MyClass()
print("*******************Math operations****************")
class MyClass():
    def values(self,val1,val2):
        print(val1,val2)
        self.val1=val1
        self.val2=val2
    def add(self):
        print(self.val1 + self.val2)
    def mul(self):
        print(self.val1*self.val2)
c=MyClass()
c.values(3,3)
c.add()
c.mul()
print("**************************Calling a method inside a method in same class*******")
class MyClass:
    def m1(self):
        print("I am from Method M1")
        self.m2(10)
    def m2(self,a):
        print("I am from Method M2:",a)
c=MyClass()
c.m1()
print("**************************constructor with variables*****************")
class MyClass():
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def add(self):
        print(self.val1+self.val2)
    def mul(self):
        print(self.val1*self.val2)
c=MyClass(10,20)
c.add()
c.mul()
print("******************************Employee details display with constructor*********")
class MyEmployee:
    def __init__(self,empid,ename,sal):
        self.empid=empid
        self.ename=ename
        self.sal=sal
    def disp(self):
        print("Employee Id:{} Employee Name:{} Employee Salary:{}".format(self.empid,self.ename,self.sal))
        print("Employee Id:%d Employee Name:%s Employee Salary:%f"%(self.empid,self.ename,self.sal))
c=MyEmployee(12345,"Ramu Gadde",10000.50)
c.disp()
print("**************************Override the method __str__() for printing reference of class******")
class MyClass:
    def __str__(self):
        return "This is refernce text"
        pass
c=MyClass()
print(c)
print("***************************Delete the instances of class by overriding __del__()********")
