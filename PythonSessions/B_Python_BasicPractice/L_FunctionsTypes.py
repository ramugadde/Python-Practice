print("*************Default arguments functions***************")
def empdetails(eid= 12345, name="Ramu Gadde", sal=10000.45):
    print(eid,name,sal)

empdetails()
empdetails(6789)
empdetails(6789,"Suchet Gadde", 1000000.45)

print("************Required Aruguments functions**************")
def empdetails(eid,name,sal):
    print("eid is:{0} ename is:{1} esal is:{2}".format(eid,name,sal))
empdetails(1,"Adroitent", 20000.34)

print("*************keyword arguments**************************")
def empdetails(empid, name, sal):
    print(empid, name, sal)
empdetails(empid=121, name= "Adroitent", sal=422200.05)

print("**************varible arguments***************************")
def disp(*a):
    for x in a:
        print(x)
disp()
disp(10)
disp(10,20)
disp(10,20,30)

print("**************varible arguments with Keyword arguments***************************")
def disp(*a, name):
    print("The name displayed is:",name)
    for x in a:
        print(x)
disp(name="Adroitent")
disp(10,name="Ramu")
disp(10,20,name="Suchet")
disp(10,20,30,name="Suchet")
