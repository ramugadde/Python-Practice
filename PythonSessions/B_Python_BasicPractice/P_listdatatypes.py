print("***********Print list and type of list**************")
l1=[10,20,30,40,50]
print(type(l1))
print(l1)

l2=[10,20,30,'Test','String List']
print(l2)

l3=[]
print(l3)

l4=list()
print(l4)

l5=list("Ramu")
print(l5)

print("**************************UNPACKING LIST*********************************")
l1=[10,10.4,"Ramu"]
a,b,c= l1
print(a,b,c)
print(type(a), type(b), type(c))
print("***************************NEXTED LIST***********************************")
l1=[[10,20],[20,30,40],[30,40,50,60]]
print(l1[0])
print(l1[0][1])
print("********************UNPACKING NESTED LIST********************************")
l1=[[1,2,3],[4,5,6,7],["ramu","gadde"]]
a,b,c = l1
print(a,b,c)
print("**************************Reterieving data from list1********************")
l1= [10,20,30,40,50,60]
for x in l1:
    print(x)
print("**************************Reterieving data from nested list2*************")
l2=[[10,20],["Ramu","Gadde"]]
for x in l2:
    print(x)
l1= [x for x in range(10)]
print(l1)
