String functions:
strip(), lstrip(), rstrip(), len()
len(): To check the lenght of the string.
strip(): To remove the blank spaces in both the sides for the string.
lstrip(): To remove the blank spaces and specified letters from the leftside.
rstrip(): To remove the blank spaces and specified letters from the rightside.
id(): prints the memory address
is, is not: memeory comparision and return boolean
==, != : data comparision and return boolean
in, not in: Checks the data available and returns boolean.

List:
1. Represents the group of objs: homogen & herogen
2. It supports indexing, forward indexing and backward indexing. Index will always starts with 0
3. Duplicate objects are allowed.
4. Insertion order should be persisted.
5. To initialize the list we need to use only []
6. List are mutable, it allows us to modify the data.
7. Sorting is possible with similar type of data.

Tuple:
1. Represents the group of objs: homogen & herogen
2. It supports indexing, forward indexing and backward indexing. Index will always starts with 0
3. Duplicate objects are allowed.
4. Tuple is immutable --> Modifications are not allowed.

Set:
1. Set is represents group of objects: Homogen & herogen
2. Set allows duplicats
3. Insertion order is not preserved.
4. There is no indexing.
5. Declare using {}
6. Set is multable. allows data modifications.
7. Nested Sets are not possible.

Dictionary:
1. Dictionary is in the form of key, value pairs, It will store both objects.
2. Each set, we can call it as item.
3. Keys must be unique and values can be duplicate.
4. Dictionary is mutable... allows modifications.
5. Reperesents with {key:value, key:value}

Overview of all the available data type sin python:

1. Number: int/float : 20,30,40,50,60   : immutable
2. String: str       : 'Ramu', "Ramu"   : immutable
3. Boolean: bool     : "True"/"False"   : immutable
4. list              : [10,20,30,40]    : mutable
5. touple            : (10,20,30,40)    : immutable
6. Set               : {10,20,30,40}    : mutable
7. Dictionary        : {111:"ramu",22:'g'}: mutable

Lambda expressions: [filter, map, reduce]
Filter: filter expects two arguments 1. Expression 2. Input.
