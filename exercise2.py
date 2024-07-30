# Quick Start with Python (Comments after pound sign won't be executed)


# 1. Python Basics: Numbers, Strings, List
## 1.1 Numbers and Arithmetic operators
1 + 2  # Addition
1 - 10  # Subtraction
10 * 2  # Multiplication
10 / 3  # the division
10 // 3  # Floor division
10 % 3  # return the remainder of the division
5 ** 2  # Exponentiation: raise 5 to the power of 2
30 - 10 * 2  # More complicated formulas

width = 20  # Assignment operators, save value to a variable
height = 5
width * height  # use the variables instead of the value

width == 20  # comparison operators ==, >, <, !=, <=, >=
width != 50
width >= 50
not width < 10  # logical operator: not, and, or
width > 10 and height == 10  # two conditions
(width > 10) and (height == 10)  # same as above
(width > 10) or (height == 10)  # alternative conditions

## 1.2 Strings
"Hello Everyone"  # double quote
'Hello Everyone'  # single quote

"doesn't"  # double quote outside, single quote inside (or reverse)
'dones\'t'  # if same quote used, use \ to escape the same quote mark inside

sentence = 'First line.\nSecond line.'  # a sentence with multiple lines: special character \n means a new line
print(sentence)  # print() gives a more readable output

# Print multiple lines using triple-quotes (select all lines and execute)
print("""         
The first line.
The second line.
The third line.
""")

# Strings can be indexed, sliced, concatenated.
len(sentence)  # check the length of a string
sentence[5]  # index character in the sixth position: python index starts from 0
sentence[-1]  # index the last character, use - to count backward
sentence[-2]  # second-last character
sentence[:3]  # first three character: index 0,1,2 only, same as sentence[0:3]
sentence[3:]  # all characters starting from the 4th
sentence[-3:]  # the last three characters

#sentence[-1] = 'H'       # strings cannot be muted, ERROR here if remove pound sign
'1st' + sentence[5:]  # replace first 5 characters by concatenating two strings.
'The 2nd ' + sentence[-5:-1] + ' only.'  # more complicated concatenation
sentence[:6] * 3 + "here"  # repeat strings with *, concatenate strings with +

## 1.3 Lists
lst = [1, 2, 3, 4, 5]

1 in lst  # membership operator: in, not in
1 not in lst

lst[0]  # list can be indexed as well
lst[3:]  # select all elements starting from the 4th.

lst + [88, 99, 100]  # concatenate two lists, original list NOT affected
lst + ['apple', 'peach']  # concatenate two lists with different data types, check the result?

lst[0] = 'one'  # unlike strings, lists are mutable.
lst.append('six')  # append new item at the end, original list is changed

# 2. Flow Control
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## 2.1 for-loop
for i in lst:
    print(i + 10)  # the body is indented (press the tab key)

## 2.2 if-else statement
if 2 in lst:
    print("We find it!")
else:
    print("We cannot find it!")

## 2.3 combine for-loop and if-else statement
for i in lst:
    if i <= 4:  # if condition, indented
        print(i, "is in the bottom.")  # indented again
    elif (i > 4) and (i <= 7):
        print(i, 'is in the middle.')
    else:
        print(i, "is in the top.")

# 3. Python functions and Modular Programming
## 3.1 Built-in functions
round(13.555, 2)
abs(-7.25)
min(5, 13, 11)
max(5, 13, 11)
pow(4, 3)  # same as 4**3


## 3.2 Define a function by yourself
def greet(name):
    """
    This function greets to the name passed in as a parameter
    :param name: string
    :return: string
    """
    print("Hello, " + name + ". How are you today?")

def compare(a, b):
    """
    compare the two numbers passed in as parameters
    :param a: number
    :param b: number
    :return: string
    """
    if a < b:
        return str(a) + " is smaller than " + str(b) + '.'  # print("{} is smaller than {}".format(a, b))
    elif a > b:
        return str(a) + " is greater than " + str(b) + '.'
    else:
        return str(a) + " is equal to " + str(b) + '.'

greet('Alice')  # apply the function with new param values
compare(2.0, 2)

##  3.3 Modular Programming
# Step1: save the above two functions in a new python script (i.e., a module) and name the file as my_module.py
# Step2: import the module in a new python script or console,  use those functions by imputing new param values
import my_module
help(my_module)
my_module.greet('Richard')    # use functions with the .method
my_module.compare(1, 2)

from my_module import greet   # import a function from a module directly
greet('Bob')

from my_module import compare
compare(3, 2)
