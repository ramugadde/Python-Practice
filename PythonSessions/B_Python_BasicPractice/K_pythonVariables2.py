'''print("************* Printing ASCII Value of a Character***************")
c= input("Enter a Character to find the ASCII Value:")
print("The ASCII value of Character {0} is:{1}".format(c,ord(c)))
print("************* Decimal to Binary Conversions*********************")
x=1001
print("The Binary value for:{0} is:{1}".format(x,bin(x)))
print("************* Decimal to Octa  Conversions*********************")
x=1001
print("The Octa decimal value for:{0} is:{1}".format(x,oct(x)))
print("************* Decimal to Hexa  Conversions*********************")
x=1001
print("The Hexa decimal value for:{0} is:{1}".format(x,hex(x)))
print("************Nonloacl keyword******************")
def parent():
    name = "Ramu Gadde"
    def child():
        nonlocal name
        name="suchet"
    print(name)
    child()
    print(name)
parent()'''

print("************Nonloacl keyword and Global variable******************")
name="New Job"
def parent():
    name = "Ramu Gadde"
    def child():
        nonlocal name
        name="suchet"
    def child1():
        global name
        name="suchet"
        print(name)
    print(name)
    child()
    print(name)
    child1()
parent()
