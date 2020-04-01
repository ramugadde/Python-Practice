print("*********WHILE Loop**********************************")
a=0
while a<10:
    print("Ramu")
    a=a+1
print("Normal program Code, not from while loop")

print("*********WHILE Loop with Elase**********************************")
a=0
while a<10:
    print("Ramu")
    a=a+1
else:
    print("Name printed Successfully: From Else")
print("Normal program Code, not from while loop")

print("*********WHILE Loop with Elase not executed.**********************************")
a=0
while a<10:
    print("Ramu")
    a=a+1
    if(a==10):
     break
else:
    print("Name printed Successfully: From Else")
print("Normal program Code, not from while loop")
