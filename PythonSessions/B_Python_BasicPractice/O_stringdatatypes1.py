#Relational operators > < >= <= == !=
print("***************** Relational operators on Strings*************")
print("Ramu" > "Jyothi")
print("Ramu" < "Jyothi")
print("Ramu" >= "Suchet")
print("Ramu" <= "Suchet")
print("Ramu" == "Jyothi")
print("Ramu" != "Suchet")
print("Ramu" == "Ramu")
print("Ramu" != "ramu")
print("******************Additional predefined funcations**************")
# upper, lower, capitalize, split, replace, join
s1= "phython Programing EXAMPLE"
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.split(" "))
print(s1.replace("EXAMPLE", "Code"))
print("+".join(s1.split()))
print("****************Enumerate function*******************************")
s1= "This is python world, Wecome everyone."
print(tuple(enumerate(s1)))
print(list(enumerate(s1)))
print("**************** starts with and Ends with************************")
str1= "Welcome to python world"
print(str1.endswith("rld"))
print(str1.endswith("to",0,10))
print(str1.startswith('Welcome'))
print(str1.startswith('come',3,10))
print("*************** Find, Index, swapcase*****************************")
str1= "Welcome To Python world!"
print(str1.find("Python"))
print(str1.find("world"))
print(str1.find("co",0,2))
print(str1.find("mo"))
print(str1.index("To"))
print(str1.index("e",0,2))
print(str1.swapcase())
print("*************** isalnum(), isalpha(), isdigit()********************")
s1 = "Python"
s2 = "Python101"
s3 = "7878958"
print(s2.isalnum())
print(s1.isalnum())
print(s3.isdigit())
print("******************** isupper(), islower(), isspace()****************")
str1= "Ramu Gadde"
str2= "RAMU GADDE"
str3= "WELCOME TO PYTHON"
str4= " "
print(str1.islower())
print(str2.isupper())
print(str3.isspace())
print(str4.isspace())
