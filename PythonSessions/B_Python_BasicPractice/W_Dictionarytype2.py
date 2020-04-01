print("*************Zip the list data ********************")
l1=[1,2,3,4,5]
l2=["A","B","C","D","E"]
x = zip(l1,l2)
d= dict(x)
print(d)

print("*************Zip the tuple data ********************")
l1=(1,2,3,4,5)
l2=("A","B","C","D","E")
x = zip(l1,l2)
d= dict(x)
print(d)

print("*************Zip the set data ********************")
l1={1,2,3,4,5}
l2={"A","B","C","D","E"}
x = zip(l1,l2)
d= dict(x)
print(d)

print("******************unpacking the set data************")
d1={111:"Ramu", 222:"Gadde"}
a,b=d1
print(a,b)
print("******************popitem, pop and clear************")
d1={111:"Ramu", 222:"Gadde", 333:"adroitent"}
print(len(d1))
print(d1.popitem())
print(d1.pop(222))
print(d1.clear())
print("*********************update dictionary***************")
d1={111:"Ramu", 222:"Gadde", 333:"Adtnt"}
d2={444: "5mcc", 555:"maxvalue", 666:"minvalue"}
d1.update(d2)
print(d1)
print("***************Concatenating data********************")
d1={111:"Ramu", 222:"Gadde", 333:"Adtnt"}
d2={444: "5mcc", 555:"maxvalue", 666:"minvalue"}
d3={**d1,**d2}
print(d3)
print("*********************Sorting on key values in Dictionary*************")
d1={333:"ramu", 444:"gadde", 111:"Mr.", 666:"5MCC", 888:"Mobile app"}
print(sorted(d1.keys()))
print(sorted(d1.values()))
for key in sorted(d1.keys()):
    print("key=%d value=%s"%(key,d1[key]))
print("********************values as None in dictionary and update the value**************")
d1={111:None , 222:"Gadde", 333:"Adroitent", 444:"5mcc"}
print(d1)
d1[111]="Ramu"
print(d1)
