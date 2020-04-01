strng = input("Enter the string:")
char1 = input("Enter the character:")
count =0
for x in strng:
    if x== char1:
        count= count+1;
print("Number of occurances is:",count)

print("***********Number of repeated words in a string****************")
str1= "This is Python Python is a language Python is easy Python"
wds = str1.split()
print("***********",wds.count())
count=0
for x in wds:
    if x == "Python":
        count = count+1
print("Number of repeated words:", count)
