Following are the basic things that we need to have an understanding about phyton.
********INSTALLATION and SETUP ENVIRONMENT PATH***********************
INSTALLATION and SETUP ENVIRONMENT PATH
•	Download and install the python from https://www.python.org
•	Once the python installation is done.
•	We need to set the path to your environment variables.
For example: C:\Users\RTDMachine\AppData\Local\Programs\Python\Python37-32

********WAYS TO RUN THE PYTHON FILES************************
1.	From Command Prompt:
a.	Go to Installation folder and click on phython.exe
b.	Should open command prompt as mentioned above.
2.	Go to command prompt and type python (Had python path in environment variables.)

Go to Command Prompt and type C:> Python
Should see the console output like this:
C:\Users\RTDMachine\Desktop\PythonPractice>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
*****************COMMENTS IN PYTHON**************************
Python comments are non execuitable code and it will ignore while executing the python program.

There are two way we can comment the code in phython.
1. Singleline comments.
2. Multiline comments.
Singleline comments: Singleline comment, we can use (Hash Symbol)# Symbol to comment singleline.
Multiline comments: Multiline comments, we can use (Three codes, Three Single codes).
"""---""" or '''---'''
************************PRINT IN PYTHON************************
To print something in console we can use "print".
In Python, ";" is not required in every statement end. Like java.
Example:
print("This is print test example.")
**********************KEYWORDS IN PYTHON************************
Following keywords are available in python.
To Find the Keywords use the following statement.

import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
*******************GENERAL DATA TYPES IN PYTHON******************
Phyton supports dynamic typing. so we need to specify any data
types while declaring the variables.
Basic Data types in python is, int, str, bool
Number : int and float : 10,20,30 10.45,20.50
String : str
Boolean: bool

In python, we can declare the strings in "" and we can declare the string in '' codes.

In Boolean, In python, True represents 1 and False represents 0.
********************INPUT DATA IN PYTHON****************************
We can use 'INPUT' to read the data from the user using python.
'INPUT' is always take data as string.
if you want to give the different type data, we need to type cast the type to desired type.
Example:
productName = input("Enter the username:")
print("Product Name is:",productName )
productId = (int)(input("Enter the productId"))
print("Product Id is:", productId)
**************************FLOW CONTROL STATEMENTS*********************
There are three types of FLOW CONTROL STATEMENTS in Phython.
1. Conditional Statements: Based on the given conditions, these statements will be executed.
1. if condition:
    pass
2. if-else
3. elif
Iteration Statements: Based on the condition, we can iterate through the given data.
1. for
2. while condition:
    pass
Transfer Statements: Transfer statements will transfer the control from one plance to another place in program.
1. break
2. continue

Discusson about range():
range(10) :         0.....9
range(4,10):        4.....9
range(4,10,3):      4,7
range(10,4,-3):     10,7

range(-10,-5):      -10,-9,-8,-7,-6
range(-10,-5,-2):   -10,-8,-6
range(-5,-10,-2):   -5,-7,-9

The following cases else block is not working.
1. break: where you are stopping execution. This case else block is not executed.
2. Exceptions: when got exceptions in loop, this case else block is not executed.
3. os._exit(0): Virtual Machine is shutdown. this cases also else block is not executed.
