print("**************Set basic example********************")
s1={1,2,3,4,5,6}
print(type(s1))
print(s1)
print("**************Hetro data********************")
s2={10,20.5,"Ramu","Set Data"}
print(s2)
print("**************empty Set********************")
s3= set()
print(s3)
print(type(s3))
print("**************tuple in Set********************")
s1={10,"Ramu",(10,20)}
print(s1)
print("***************Adding,Update data to set*************")
s1={10,20,30,40,50}
s1.add(60)
print(s1)
s1.update([70,80]) #List
print(s1)
s1.update((90,100)) #Tuple
print(s1)
s1.update({110,120})#Set
print(s1)
print("********************copying the set data*************")
s1={10,20,30,40,50,60}
s2=s1.copy()
print(s1)
print(s2)
print("***************** Set iteration***********************")
s1={10,20,30,40,50}
for x in s1:
    print(x)
print("***************** Set stoping on condition***********************")
for x in s1:
    if(x==20):
        break
    print(x)
print("***********Printing the id-> memory address, is, is not -> memory comparision****")
s1={10,20,30,40,50,60}
s2={70,80,90,100,110}
s3={10,20,30,40,50,60}
s4=s1
print(s1 is s2)
print(s4 is s1)
print (s4 is not s1)
print(s1==s3)
print(s1!=s3)
print(id(s1))
print(id(s4))
print(0 in s1)
print(0 not in s1)
print("*******************add 1 to 10 elements to set***********************")
n=(int)(input("Enter the number for range:"))
s1={x for x in range(n)}
print(s1)
print("***************** Remove, pop, discard, clear of the element from set***********************")
s1={10,20,30,40}
s1.remove(10)
print(s1)
s1.pop()
print(s1)
s1.discard(40)
print(s1)
