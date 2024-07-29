# Quick Start with Python (Comments after pound sign won't be executed)

# 1. Using Python as a Calculator
# 1.1 Numbers and Arithmetic operators
1 + 2     # Addition
1 - 10    # Subtraction
10 * 2    # Multiplication
10/3      # the division
10//3     # Floor division
10 % 3    # return the remainder of the division
5 ** 2    # Exponentiation: raise 5 to the power of 2
30 - 10 * 2   # More complicated formulas

width = 20        # Assignment operators, save value to a variable
height = 5 
width * height    # use the variables instead of the value

width == 20       # comparison operators ==, >, <, !=, <=, >=
width != 50
width >= 50
not width < 10    # logical operator: not, and, or
width > 10 and height == 10      # two conditions
(width > 10) and (height == 10)  # same as above
(width > 10) or (height == 10)   # alternative conditions


# 1.2 Strings
"Hello Everyone"        # double quote
'Hello Everyone'        # single quote

"doesn't"               # double quote outside, single quote inside (or reverse)
'dones\'t'              # if same quote used, use \ to escape the same quote mark inside

sentence = 'First line.\nSecond line.'   # a sentence with multiple lines: special character \n means a new line
print(sentence)                          # print() gives a more readable output

print("""         
The first line:
The second line:
The third line:
""")              # print multiple lines using triple-quotes.

# Strings can be indexed, sliced, concatenated.
len(sentence)  # check the length of a string
sentence[0]    # index the first position of the string: python index starts from 0
sentence[5]    # the character in the sixth position
sentence[-1]   # last character, use - to count backward
sentence[-2]   # second-last character
sentence[:3]   # first three character: index 0,1,2 only, same as sentence[0:3]
sentence[3:]   # all characters starting from the 4th
sentence[-3:]  # the last three characters

#sentence[-1] = 'H'       # strings cannot be muted, ERROR here if remove pound sign (check error message in python console)
'1st' + sentence[5:]      # replace first 5 characters by concatenating two strings.
'The 2nd ' + sentence[-5:-1] + ' only.'   # More complicated concatenation
sentence[:6] * 3 + "here"                # repeat strings with *, concatenate strings with +


# 1.3 Lists
lst = [1, 2, 3, 4, 5]

1 in lst        # membership operator: in, not in
1 not in lst

lst[0]          # list can be indexed as well
lst[3:]         # select all elements starting from the 4th.

lst + [88, 99, 100]          # concatenate two lists, original list NOT affected
lst + ['apple', 'peach']     # concatenate two lists with different data types, check the result?

lst[0] = 'one'               # unlike strings, lists are mutable.
lst[1:3] = ['two', 'three']  # replace 2nd and 3rd elements together
lst.append('six')            # append new item at the end, original list is changed



# 2. Flow Control
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for-loop
for i in lst:
    print(i + 10)     # the body is indented (press the tab key)

# if-else statement
if 2 in lst:
    print("We find it!")
else:
    print("We cannot find it!")

# combine for-loop and if-else statement
for i in lst:
    if i <= 4:                           # if condition, indented
        print(i, "is in the bottom.")    # indented again
    elif (i > 4) and (i <= 7):
        print(i, 'is in the middle.')
    else:
        print(i, "is in the top.")



# 3. Python functions and Modular Programming
## 3.1 Some built-in functions
round(13.555, 2)
abs(-7.25)
min(5,13,11)
max(5,13,11)
pow(4,3)       # same as 4**3

## 3.2 Define a function by yourself
def greet(name):
    """
    This function greets to the person
    passed in as a parameter
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
        return str(a) + " is smaller than " + str(b) + '.'   # print("{} is smaller than {}".format(a, b))
    elif a > b:
        return str(a) + " is greater than " + str(b) + '.'
    else:
        return str(a) + " is equal to " + str(b) + '.'


greet('Elijah')           # use the function defined above
compare(2.0, 2)


##  3.3 Modular Programming
# Save the above two functions in a separate python script (that is a module) and name the file as my_module.py
# Import the module and use its functions in a new script (or in Python console) with below codes
import my_module
help(my_module)
my_module.greet('Richard')
my_module.greet('Grace')
my_module.compare(1,2)
my_module.compare(5,2)
my_module.compare(2.0,2)

from my_module import greet      # import a function from a module directly
greet('Bob')

from my_module import compare
compare(1,2)