#Inheritance is acquiring the properties of parent class to child class.
class MyCars:
    def models(self):
        print("Car Models:")
        print("BMW")
        print("i20")
        print("Verna")
    def price(self):
        print("Prices of car models:")
        print("4000000")
        print("1000000")
        print("2500000")
class MyDetails(MyCars):
    def carDetails(self):
        print("***********From child class method**********")
        print("This is from car details class as child")
c= MyCars()
c.models()
c.price()
print("********************From Inherited class***************")
d=MyDetails()
d.models()
d.price()
d.carDetails()
print("************************Calling super class methods using SUPER in child class************")
class MyParent:
    def myParentMethod(self):
        print("this is parent class method")
class MyChild(MyParent):
    def myChildMethod(self):
        print("This is my child method")
        super().myParentMethod()
c=MyChild()
c.myChildMethod()
print("****************************Super class variables*******************************************")
class MyParent1:
    a,b=10,20
class Child(MyParent1):
    x,y=100,250
    def add(self,i,j):
        print(i+j)
        print(self.x+self.y)
        print(self.a+self.b)
c=Child()
c.add(200,200)
print("******************************Super class variables with same name****************************")
class MyParent1:
    a,b=10,20
class Child(MyParent1):
    a,b=100,250
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(super().a+super().b)
c=Child()
c.add(200,200)
print("****************************Constructor********************************")
class MyParent:
    def __init__(self):
        print("this is from parent class constructor")
class MyChild(MyParent):
    pass

c= MyParent()
print("****************************calling child calls Constructor********************************")
class MyParent:
    def __init__(self):
        print("this is from parent class constructor")
class MyChild(MyParent):
    def __init__(self):
        print("this is from child class constructor")

c= MyChild()

print("****************************calling parent calls Constructor in child class********************************")
class MyParent:
    def __init__(self, name):
        print("this is from parent class constructor",name)
class MyChild(MyParent):
    def __init__(self):
        print("this is from child class constructor")
        super().__init__("ramu")
c= MyChild()
