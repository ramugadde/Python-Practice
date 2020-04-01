import os
print("*******Print Numbers upto 10**************")
print("One two ten numbers are:")
for x in range(10):
    print(x)

print("*****Numbers upto given number************")
valn = (int)(input("Enter the value to print numbers:"))
print("Numbers upto:",valn)
for x in range(valn):
 print(x)

print("*****Even numbers upto given number************")
valn = (int)(input("Enter the value to print numbers:"))
print("Numbers upto:",valn)
for x in range(0,valn,2):
 print(x)

print("*****Odd numbers upto given number************")
valn = (int)(input("Enter the value to print numbers:"))
print("Numbers upto:",valn)
for x in range(1,valn,2):
 print(x)

print("*****Numbers upto given number in reverse order************")
valn = (int)(input("Enter the value to print numbers:"))
print("Numbers upto:",valn)
for x in range(valn,0,-1):
 print(x)

print("********** For With Else***********************************")
nm= (int)(input("Enter the number:"))
for x in range(nm):
    print(x)
else:
    print("Successfully printed the numbers.")

print("*********For with Else****$$$Else not executed$$$***")
nm= (int)(input("Enter the number:"))
for x in range(nm):
    print(x)
    os._exit(0)
else:
    print("Successfully printed the numbers.")
