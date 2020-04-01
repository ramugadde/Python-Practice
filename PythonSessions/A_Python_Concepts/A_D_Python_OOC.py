Class: class is collection of objects. Class is a blue print, Class is logical entity.
2. Class is blue print and it decides objects creation.
3. Class can allow to create a multiple objects.
4. Every object occupies memory.
5. Decleare the class using "class" keyword.
phython 2.7:
class MyClass:
    pass
class MyClass():
    pass
class MyClass(object)
    pass
6. To specify the methods to recognize from the same class, we can use key word "self"
7. Constructor is a method which initiated when the instance is created to a class.
   Example:
    def __init__(self):
        print("This is from constructor")
8. To convert local varibles into class levl variables. we can use "self" keyword.
   Example:
    def add(val1, val2):
        print(self.val1,self.val2)
    def mul(val1, val2):
        print(self.val1* self.val2)
9. Inheritance: the process of acquiring the properties of existing class to new class.
10. Types of inheritance.
    1. single inheritance: one parent class contains once child class.
    2. multilevl inheritance: Parent call -> child class -> sub Child class.
    3. Multiple inheritance --> On Child with multiple parent classes.
    4. hirarchical Interitance -> one parent class with multiple child classes.
    5. hybrid inheritance -> combination 3 & 4
