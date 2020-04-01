print("******************Basic class************************")
class MyClass1:
    pass
class MyClass2():
    pass
class MyClass3(object):
    pass
print(issubclass(MyClass1, object))
print(issubclass(MyClass2, object))
print(issubclass(MyClass3, object))
print("*****************Sample Class with functions*************")
class MyGreeting:
    def disp1(self):
        print("Hi.....Good morning!!!!!")
    def disp2(self, name):
        print("Hi....:",name,"Good Evening")
c= MyGreeting()
c.disp1()
c.disp2("Ramu")
print("*******************Instacne and static method************")
class MyClass:
    def m1(self):
        print("Instance mehtod")
    @staticmethod
    def m2():
        print("static method")
c=MyClass()
c.m1()
MyClass.m2()
print("*******************Class varibales************")
class MyClass:
    a,b=10,20
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
c=MyClass()
c.add()
c.mul()
print("***********************Local variables, Class varibles, Global veariables***********************")
i,j=100,200
class MyClass:
    a,b=10,20
    def add(self,x,y):
        print(x+y)
        print(self.a+self.b)
        print(i+j)
    def mul(self,x,y):
        print(x*y)
        print(self.a*self.b)
        print(i*j)
c=MyClass()
c.add(2,2)
c.mul(4,4)
print("***********************Local variables, Class varibles, Global veariables with same names***********************")
a,b=100,200
class MyClass:
    a,b=10,20
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])
    def mul(self,a,b):
        print(a*b)
        print(self.a*self.b)
        print(globals()['a']*globals()['b'])
c=MyClass()
c.add(2,2)
c.mul(4,4)
print("*******************************multiple objects for single class**************")
class MyClass:
    def disp(self):
        print("Good Morining")
c=MyClass()
c1=MyClass()
c.disp()
c1.disp()
MyClass().disp()
print("*******************************Named and Nameless objects*********************")
class MyClass:
    def disp(self):
        print("Good Morining")
MyClass().disp()
