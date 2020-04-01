print("*******Single Inheritance********************")
class MyParent:
    def myParentMethod(self):
        print("This is my first parent method")
class MyChild(MyParent):
    def myChildMethod(self):
        print("this is my first child method")
c=MyChild()
c.myParentMethod();
c.myChildMethod();
print("***********mutileve Inheritance****************")
class MyCars:
    def carNames(self):
        print("BMW","GM","BENZ","MINI")
class MyPrice(MyCars):
    def carPrice(self):
        print("12000","340000","4500000")
class MyCarDetails(MyPrice):
    def allCarDetails(self):
        super().carNames()
        super().carPrice()
c=MyCarDetails()
c.allCarDetails()
print("***********Multiple Inheritance****************")
class MyCars:
    a,b=10,20
    def carNames(self):
        print(a,b)
        print("BMW","GM","BENZ","MINI")
class MyPrice():
    def carPrice(self):
        print("12000","340000","4500000")
class MyCarDetails(MyCars,MyPrice):
    def allCarDetails(self):
        print("This is from Child")
c=MyCarDetails()
c.carNames()
c.carPrice()
c.allCarDetails()
