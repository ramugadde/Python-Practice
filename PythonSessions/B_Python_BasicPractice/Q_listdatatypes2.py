print("************* List with duplicate data********")
l1=[10,10,10,10]
print(l1)
print("************Add Data to existing List*********")
#Concatenate
l1=[10,30,40]
l2=[50,60,70]
l3=l1+l2
print(l3)
#Replication
l1= [10,30,40]
l2=l1*2
print(l2)
#Copy
l1=[10,20,30]
l2=l1.copy()
l3=l1+l2
print(l3)
#extend
l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2)
print(l1)
#append
l1=[10,20,30,40]
l1.append(50)
print(l1)
#insert
l1=[10,20,30,40]
l1.insert(0,5)
print(l1)
#Remove the Data
l1=[10,20,30,40]
l1.remove(10)
print(l1)
#pop
l1=["Ramu","Gadde", "ravi","Adroitent"]
l1.pop()
print(l1)
#Delete
l1=[10,20,30,40,50]
del (l1[1])
print(l1)
#Clear
l1=[10,20,30,40,50]
l1.clear()
print(l1)
