#Variable is a container to store a value.
a = 2345 #Here, 'a' is a variable and 2345 is a integer literal stored in a memory location named 'a'.
print(a)

#in python, string can also be enclosed in single quote and triple quote
b = 'Seemana' 
print(b)

c = "Seemana"
print(c)

#when we use triple quote to enclose string, we can write double quote and single quote as a part of the string
d = '''Se"em'ana''' 
print(d)

'''
Data Types in Python
1. Integers
2. Floating point numbers
3. Strings
4. Booleans
5. None

PYTHON automatically IDENTIFIES the type of data for us. We don't need to write it's datatype like int a = 5 as in other programming languages.

a = 57 --> identifies a as class <int>
b = "Seemana" --> identifies b as class <string>
c = 24.87 --> identifies c as class <float>

'''

print(type(d)) #it prints the datatype of literal stored in variable 'd' as <class 'str'>

