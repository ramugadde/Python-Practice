print("*********** Method@1(if statement)*********************")
x=40
if x>0:
    print("Yes, X > Zero and X values is:",x)
print("!!!!out of if statement!!!!!")

print("*********** Method@2(If else)*********************")
num= (int)(input("Enter the number:"))
if num >=0:
    print("Given number is:",num," Grater than Zero")
else:
    print("Given number is:",num," Less than Zero")
print("!!!!out of if statement!!!!!")

print("*********** Method@3(if else single statement) *********************")
{print("if statement:True"), print("if statement:True1")} if True else {print("if statement:False"),print("if statement:False1")}

print("*********************** Method@4(elif)*******************************")
tn = (int)(input("Enter a number:"))
if (tn%2 == 0):
    print("{0} is Even number".format(tn))
elif(tn%2 == 1):
    print("{0} is Odd number".format(tn))
else:
    print("Gien number is invalid")
