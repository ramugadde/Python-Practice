print("************Function*********************")
def disp1():
    print("Good morning")
def disp2(name):
    print("Good evening", name)
disp1()
disp2("Ramu")
'''print("************Function with Local Variables*********************")
def disp1():
    name="Ramu"
    print("Good morning")
def disp2():
    print("Good evening", name)
disp1()
disp2()'''
print("************Function with Global Variables*********************")
name="PYTHON"
def disp1():
    print("Good morning")
def disp2():
    print("Good evening", name)
disp1()
disp2()

print("************Function with Global Variables*********************")
a,b=10,20
def add(x,y):
    print("Addition of X,Y is:",x+y)
    print("Addition of A,B is:",a+b)
def mul(x,y):
    print("Multiplication of X,Y is:",x*y)
    print("Multiplication of A,B is:",a*b)
add(3,4)
mul(30,40)

print("************Function with Global Variables With Same name.*********************")
a,b=10,20
def add(a,b):
    print("Addition of Gloal A,B is:",globals()['a']+globals()['b'])
    print("Addition of A,B is:",a+b)
def mul(a,b):
    print("Multiplication of Global A,B is:",globals()['a']*globals()['b'])
    print("Multiplication of A,B is:",a*b)
add(3,4)
mul(30,40)
print("*********************Format using separator***************************")
print(10,20,30,40,50, sep='+')
