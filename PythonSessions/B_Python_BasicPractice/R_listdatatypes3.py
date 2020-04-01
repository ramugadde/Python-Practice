print("***************Printing the first values from sublist**********")
l1=[[1,2],["Ramu","Gadde"],[10.5,20.5]]
l3=[]
l4=[]
for x,y in l1:
    l3.append(x)
    l4.append(y)
print(l3)
print(l4)
print("**********************Sorting of the list**********************")
l1=[2,4,1,5,20,10,15,11,25,30]
l1.sort()
print(l1)
print("**********************ReverseOrder of the list*****************")
l1.sort(reverse=True)
print(l1)
print("***********************index************************************")
l1=["Ramu", "Gadde","Adroitent","Gadde"]
print(l1.index("Ramu"))
print(l1.index("Gadde",2))
print(l1.index("Adroitent",1,4))
print("********************** Count of data ****************************")
l1=[10,20,30,10,30,30,30,40,40,50,50]
x=l1.count(30)
print(x)
print("********************** Length of List ****************************")
l1=[10,20,30,10,30,30,30,40,40,50,50,"Ramu","Gadde","Test","Max"]
x=len(l1)
print(x)
print("********************** Max and Min of List ****************************")
l1=[10,20,30,10,30,30,30,40,40,50,50,1000,-1]
maxn= max(l1)
minn= min(l1)
print(maxn, minn)
