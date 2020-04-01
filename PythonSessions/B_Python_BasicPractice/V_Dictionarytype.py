print("********* Sample dictionary********************")
d1={111:"ramu",222:"Gadde",333:"Adroitent"}
print(d1)
print(type(d1))
print("**************Create a empty dictionary and add data*******")
d1={}
d1[11]="Ramu"
d1[22]="Gadde"
d1[33]="Adroitent"
d1[44]="Python"
d1[55]="Test"
print(d1)
print("**************print only Keys and Only values*******")
d1={111:"ramu",222:"Gadde",333:"Adroitent"}
print("*******************Data in list format****************")
print(list(d1.keys()))
print(list(d1.values()))
print(list(d1.items()))
print("*******************Data in touple format*********************")
print(tuple(d1.keys()))
print(tuple(d1.values()))
print(tuple(d1.items()))
print("***************Data in set format*****************************")
print(set(d1.keys()))
print(set(d1.values()))
print(set(d1.items()))
print("***************Print the data using loop**********************")
d1={111:"Ramu",222:"Gadde",333:"Adroitent",444:"5MCC",555:"Mobile",666:"Application"}
for x in d1:
    print(x, d1[x])
print("******** Printing data in 2nd method**************************")
d1={111:"Ramu",222:"Gadde",333:"Adroitent",444:"5MCC",555:"Mobile",666:"Application"}
for x,y in d1.items():
    print(x,y)
print("******** Printing data in 3rd method**************************")
d1={111:"Ramu",222:"Gadde",333:"Adroitent",444:"5MCC",555:"Mobile",666:"Application"}
for x,y in d1.items():
    print(d1.get(x))
