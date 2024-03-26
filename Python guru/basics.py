'''these are itegers and they are part of the data types used in python together with others,
1, 2, 3, and so on then we have another set of data types that is floating point number which basically have a decimal point. Then we have strings which are basically set of words or sentencess that are eecutable in code and they're mostly desirable
from the user's pov. Then another set is boolean this is absically true and false.

THERE ARE ALSO ARITHMETIC OPERATORS
These are a piece of cae like the rest of them: +, -, /, //, *, %

Variables
they are names given to data ites that may take on one or more values during a program's runtime. E.G:'''
'''
var = "Score"
print(var)
first_name = "Masai"
print("my first name is " + first_name) '''

''' more math functions
pow - gives you the power t that number
min - gives yu the smallest number
max - gives you the largest number
round - gives you the rounded off number
from math import *
print(pow(2, 10))'''

'''let's look at conditional statements. eg: If statement, elif, else let's look at an example of them
in a practical pov'''

'''
var = "90"
if var != "90":
    print("Great")
elif var > "90":
    print("Meh")
else:
    print("Pull up your socks") '''

'''Now let's explore loop statements! FFUUUUUN!!!
For loop, for with range, for with range(start, stop, step), for with in, whille loops eg:'''
'''jump statements break, continue, pass, return. they do wonders check them out'''
'''for i in range(9):
    if i%44 == 5:
        pass
    else:
        print(i)'''
'''this is for the return statement'''
'''
def fun(x):
    if x != 'Hello':
        return True
    else:
        return False'''

'''functions in python '''
'''
def fun(a,b):
    return a+b
def printsum(a, b):
    print(a+b)
print(fun(3, 4))
printsum(3, 4) 
'''
'''global statement'''
'''
def fun():
    global Value
    value = "Local"
value = "Global"
fun()
print(value) '''
'''
song = "Vivaldi four seasons"
drink = "hibiscus tea"
read = "sora"
print("This: " + song + "," + drink + "," +  "and the OpenAI " + read  + " gives a perfect friday night!")'''
'''
import math
print(math.c)'''
''''
def divide(a, denominator):
    try:
        return a / denominator
    except ZeroDivisionError as e:
        print("Divide by zero!! Terminate!!")
    finally:
        print("Division complete!")
        
        WILL GET BACK TO LATER'''
'''
#these are lists
subjects = ["English, French, Spanish, Computer"];
print(subjects)
#positive slicing
print(subjects[0], subjects[-1])
#negative slicing
print(subjects[0:2], subjects[-3:-1])

#changing values in a list
print(subjects)
subjects[-1] = "Java"
print(subjects)

# trying to solve a kata here
values = [1, 2, 3, 4, 5];
if values == 2:
    print(2) #still a work in progress but i'll figure it out
else:
    print(values)
    values[4] = "2"
    print(values)

#replication
subjects = subjects * 4
print(subjects)

#concatenation
subjects = subjects + values
print(subjects)

#deleting stuff like people lol
print(values)
del values[0:3]
print (values)

#loop through lists
for ex in values:
    print(values)
else:
    print(subjects)

#not and in keywords
print("2" in values)
print("fine" in subjects)

#inert()
print(subjects)
subjects.insert(0, 'happy')
print(subjects)

#apped()
print(subjects)
subjects.append('the last')
print(subjects)
'''
'''
#lastly in lists, sorting
subjects = [1, 2, 3, 4, 5]
subjects.sort()
print(subjects)

#descending order
subjects.sort(reverse = True)
print(subjects)
'''
'''
#tuples
example = ('1', '2', '3')

print(example[1:2])
'''
'''
#dictionaries keys and values
dict = {'first' :'Saturday', 'second' : 'Monday', 'third' : 'Tuesday'}
for key in dict.keys():
    print(key)
for value in dict.values():
    print(value)'''

'''
dict1 = {'first' : 'Sunday', 'Third' : 'Monday', 'Fourth' : 'Tuesday'}
dict2 = {'one': 'happy', 'two': 'sad' , 'three': 'moody'}
dict1.update(dict2)
print(dict1)
'''
'''
#sets in python
s = {1, 2, 3, 4}
print(s)
s.update([1, 0, 12,13])
print(s)
s.discard(13)
print(s)
'''
'''
# operator in sets & | - ^
a = {1, 2, 3, 4, 5, 5, 6, 6}
b = {1, 2, 5, 7, 8}
print(a & b)
print(a | b)
print(a ^ b)
print(a - b)
'''
'''
#list comprehensions
a = [0,1,2,3]
#b will store values which are greater than 1 in a
b = [i+1 for i in a]
print(b)

#set comprehension
a = {1, 2, 3, 4, 5}
#b will store squares of the elements of a
b = {i **2 for i in a}
print(b)

#dict comprehension
a = {'hello':'world', 'first' : 'happy'}
#b will stores elements of a in value-key format
b = {val: k for k, val in a.items()}
print(b)
'''
'''
#string manipulation
#multiline strings
a = ''''''i am happy today, so happy in jesus name''''''
print(a)
#string indexing
a = "happy"
print(a[0], a[1], a[2])
print(a[-2], a[-1])

#strings slicing
a = "DONE"
print(a[0:3])
print(a[-3:-1])
print(a[1:3])
'''
'''
#case conversion functions
a = "Hello"
print(a.islower())
print(a.upper())
print(a.isupper())
print(a.lower())
'''
'''
#join and pslit function
list = ["one", "two", "three"]
#join function
s = ','.join(list)
print(s)
#split function
newlist = s.split(',')
print(newlist)
'''
'''
#string formatting
first = "first"
second = "second"
s = "Sunday is the {} day of the week and Monday is the {} day of the week".format
print(s)
'''
'''
from string import Template
name ='Scaler'
t = Template('Hey $name!')
t.substitute(name=name)'''