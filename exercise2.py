# Quick Start with Python (Comments after pound sign won't be executed)


# 1. Python Basics: Numbers, Strings, List
## 1.1 Numbers and Arithmetic operators
1 + 2        # Addition
1 - 10       # Subtraction
10 * 2       # Multiplication
10 / 3       # Division
5 ** 2       # Exponentiation: raise 5 to the power of 2
30 - 10 * 2  # More complicated formulas

width = 20      # Assignment operators, assign a value to a newly created variable
height = 5
width * height  # Use the variables instead of the value

width == 20     # Comparison operators ==, >, <, !=, <=, >=
width != 50
width >= 50

not width < 10                   # Logical operator: not, and, or
(width > 10) and (height == 10)  # Two conditions, same as width > 10 and height == 10
(width > 10) or (height == 10)   # Alternative conditions

## 1.2 Strings
"Hello Everyone"  # Double quote
'Hello Everyone'  # Single quote

"doesn't"         # Double quote outside, single quote inside (or reverse)
'dones\'t'        # If same quote used, use \ to escape the same quote mark inside

sentence = 'First line.\nSecond line.'  # Create a sentence with multiple lines: special character \n means a new line
print(sentence)                         # The print() gives a more readable output

# Print multiple lines using triple-quotes (select all lines and execute)
print("""         
The first line.
The second line.
The third line.
""")

# Strings can be indexed, sliced, concatenated.
len(sentence)  # Check the length of a string
sentence[5]  # Select character in the sixth position: python index starts from 0
sentence[-1]  # Select the last character, use - to count backward
sentence[-2]  # Select the second-last character
sentence[:3]  # Select first three character: index 0,1,2 only, same as sentence[0:3]
sentence[3:]  # Select all characters starting from the 4th
sentence[-3:]  # Select the last three characters

#sentence[-1] = 'H'                      # Strings cannot be muted, ERROR here if executed
'1st' + sentence[5:]                     # Replace first 5 characters by concatenating two strings.
'The 2nd ' + sentence[-5:-1] + ' only.'  # More complicated concatenation
sentence[:6] * 3 + "here"                # Repeat strings with *, concatenate strings with +

## 1.3 Lists
lst = [1, 2, 3, 4, 5]      # Create a variable lst

1 in lst                   # Membership operators: in, not in
1 not in lst

lst[0]                     # Lists can be indexed as well
lst[3:]                    # Select all elements starting from the 4th

lst + [88, 99, 100]        # Concatenate two lists, the original list is NOT affected
lst + ['apple', 'peach']   # Concatenate two lists with different data types, check the result?

lst[0] = 'one'             # Unlike strings, lists are mutable.
lst.append('six')          # Append a new item at the end, original list is changed


# 2. Flow Control
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # Create another variable lst2

## 2.1 The for-loop (select all lines and execute)
for i in lst2:
    print(i + 10)     # Indented (press the tab key)

## 2.2 The if-else statement
if 2 in lst2:
    print("We find it!")
else:
    print("We cannot find it!")

## 2.3 Combine for-loop and if-else statement
for i in lst2:
    if i <= 4:  # 1st indentation
        print(i, "is in the bottom.")  # 2nd indentation
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

## 3.2 Define a custom function by yourself
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
## Step 1: save the above two functions in a new python script (i.e., a module) and name the file as my_module.py
## Step 2: import the module in a new python script or console,  use those functions by imputing new param values
import my_module
help(my_module)
my_module.greet('Richard')   # Use functions after the module name with the .method
my_module.compare(1, 2)

from my_module import greet  # Import a function from a module directly
greet('Alice')

from my_module import compare
compare(3, 2)
