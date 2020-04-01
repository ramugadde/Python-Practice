print("******************print type of string*****************")
myStr = "This is sample string"
print(myStr)
print(type(myStr))
print("******************String positive indexing*****************")
myStr = "ADROITENT"
print(myStr[2])   #printing 2nd letter is: O,1,2 i.e, R
print(myStr[2:])  #printing 2nd position to end for the string.
print(myStr[0:8]) #printing Oth position to 8th position.
print(myStr[2:8:2]) #printing, every 2nd letter after R and before T
print(myStr[:5]) #printing from start to 5 letters.
print(myStr[:]) #prining the entire string.
#print(myStr[40]) #throws outof bounds exception.
print("******************String functions*****************")
s = "@@@@@@@ADROITENT$$$$$$$$K"
print(len(s))
print(len(s.strip()))
print(s.rstrip("K"))
print(s.lstrip("@").rstrip("$K"))
print("******************String functions(id,is, is not, in, not in)*****************")
str1="adroitent"
str2="technology"
str3="adroitent"
print("************** ID ***********")
print(id(str1))
print(id(str2))
print(id(str3))
print("************** is, is not ***********")
print(str1 is str2)
print(str1 is str3)
print(str1 is not str2)
print(str1 is not str3)
print("************** ==, != ***********")
print(str1 == str2)
print(str2 == str3)
print(str1 != str2)
print(str2 != str3)
print("************** in, not in ***********")
print("adro" in str1)
print("ramu" not in str1)
print("adro" not in str1)
print("*******Concatenation and replication")
s1= "adroitent "
s2= " ites"
s3= " pvt ltd"
s4= s1+s2+s3
print(s4)
print(s1*3)
