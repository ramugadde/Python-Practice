def m1(x):
    print(2*x)
m1(10)
print("******************Lambda basic example**************************")
a=lambda x:x*2
print(a(10))
print("******************Lambda with 2 parameters example**************")
a=lambda x,y: x*y
print(a(10,20))
print("*****************Lambda with condition**************************")
a= lambda x,y: x if x>y else y
print(a(8,7))
print("***************Filter the data**********************************")
l1=[10,2,3,4,5,7,8,6,1]
def m1(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(m1,l1)))
print("***************Lambda the data***********************************")
print(list(filter(lambda x:x%2==0,l1)))
print("********************Filster string*******************************")
l1=["ramu", "Test","ramu"]
def m1(x):
    if x =="ramu":
        return True
    else:
        return False
print(list(filter(m1,l1)))
print("***********************Lambda expression**************************")
l2=list(filter((lambda x: x=='ramu'),l1))
print(l2)
print("************************Mapper************************************")
l1=[1,2,3,4,5,6,7,8]
def m1(x):
    return x*5
print(list(map(m1,l1)))
print("*********lambda map***********************************************")
print(list(map(lambda x:x*5,l1)))
print("**************Appending text to exising string********************")
l1=["ramu","suchet","jyothi"]
def m1(x):
    return x+"it"
print(list(map(m1,l1)))
print(list(map(lambda x: x+'it', l1)))
print("****************print two lists as single list*****************")
l1=[1,2,3,4]
l2=[10,20,30,40]
l3=[100,200,300,400]
print(list(map(lambda x,y:x+y, l1,l2)))
print(tuple(map(lambda x,y:x+y, l1,l2)))
print(set(map(lambda x,y:x+y, l1,l2)))
print("**********print the lenght of each word in sting*************")
s="Hi Ramu how is adroitent job."
words=s.split()
for x in words:
    print(len(x))
print(list(map(lambda x: len(x), words)))
print("***************************Reduce:functools*****************")
from functools import reduce
l1=[24,35,45,30,40,60]
prod = 0
for x in l1:
    prod= prod + x
print(prod)
print(reduce(lambda x,y: x+y,l1))
print(reduce(lambda x,y: x+y, range(1,100)))
