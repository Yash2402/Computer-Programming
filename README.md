## Assignment 1:
***
Install python and set up the development environment.; Write a python program to print "Hello World!"; Write a python program to calculate the area of a circle given the radius.
PYTHON ENVIRONMENT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3
Python 3.12.1 | packaged by conda-forge | (main, Dec 23 2023, 08:01:35) [Clang 16.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
CODE:
```python
print("Hello World!")

import math
radius = int(input("Enter the radius of the circle: "))
print(math.pi * radius * radius) 
```

OUTPUT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment1.py
Hello World!
Enter the radius of the circle: 45
6361.725123519332
```
## Assignment 2:
***
Write a Python program to check if a number is even or odd,; Implement a simple calculator using conditional statements; Write a python program to print the Fibonacci series using a for loop.
CODE:
```python
# Checking a number for being odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# A simple calculator
def calculate(num1, operator, num2):
    """
    Performs basic arithmetic operations based on the provided operator.

    Args:
        num1: First operand (float).
        operator: Mathematical operator (string).
        num2: Second operand (float).

    Returns:
        The result of the calculation (float).
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cant divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"


while True:
    # Get user input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform calculation and handle errors
    result = calculate(num1, operator, num2)

    # Print the result
    print(result)

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
        break

print("Thank you for using the calculator!")


# Printing the Fibonacci
def fibonacci(n):
    """
    Prints the Fibonacci series up to the nth term.

    Args:
        n: Number of terms to print (integer).
    """
    # Initialize first two terms
    a, b = 0, 1

    # Print the first two terms if n is greater than or equal to 2
    if n >= 2:
        print(a, b, end=" ")

    # Iterate for n-2 times to print remaining terms
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c


# Get user input for number of terms
num_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci series
fibonacci(num_terms)

print("\n")
```
OUTPUT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment2.py
Enter a number: 5
5 is odd
Enter the first number: 45
Enter the operator (+, -, *, /): /
Enter the second number: 34
1.3235294117647058
Do you want to perform another calculation? (y/n): n
Thank you for using the calculator!
Enter the number of terms: 20
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
```
## Assignment 3:
***
Implement a function to check if a given string is palindrome,; Perform various operations on lists (e.g. sorting, slicing),; Use dictionaries to store and retrieve student grades.
CODE:
```python
# Checking whether a string is palindrome or not
string = input("Enter a string to checking if it is palindrome or not: ")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

# List Operations
lst = [20, 4, 65, 345, 34, 567, 324, 8, 42, 432, 86, 42, 5756]
print("lst =", lst)
lst.sort()
print("Sorted:", lst)
lst.pop(2)
print("lst.pop(2)", lst)
print("lst.index(8):", lst.index(8))
newlst = lst[2:7:2]
print("Slicing:", newlst)

# Use dictionaries to store and retrieve student grades.
stu_data = {}
n = int(input("Enter number of students you want to store the data of: "))
for _ in range(n):
    name = input("Enter the name: ")
    rollno = input("Enter the roll no: ")
    branch = input("Enter the branch: ")
    stu_data[rollno] = [name, branch]

run = True
while run:
    search = input("Enter the roll no of the student you want to search: ")
    if search in list(stu_data.keys()):
        print(
            f"Name: {stu_data[search][0]}\nRoll No: {search}\nBranch: {stu_data[search][1]}"
        )
    else:
        print("404: Student Not Found!")
    run = 1 - int(input("Do you want to exit [1(yes)/0(no)]: "))
```
OUTPUT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment3.py
Enter a string to checking if it is palindrome or not: noon
noon is a palindrome.
lst = [20, 4, 65, 345, 34, 567, 324, 8, 42, 432, 86, 42, 5756]
Sorted: [4, 8, 20, 34, 42, 42, 65, 86, 324, 345, 432, 567, 5756]
lst.pop(2) [4, 8, 34, 42, 42, 65, 86, 324, 345, 432, 567, 5756]
lst.index(8): 1
Slicing: [34, 42, 86]
Enter number of students you want to store the data of: 2
Enter the name: Yash
Enter the roll no: 2023UME4063
Enter the branch: ME
Enter the name: Bhavya
Enter the roll no: 2023UME4062
Enter the branch: ME
Enter the roll no of the student you want to search: 2023UME4062
Name: Bhavya
Roll No: 2023UME4062
Branch: ME
Do you want to exit [1(yes)/0(no)]: 0
Enter the roll no of the student you want to search: 2023UME4094
404: Student Not Found!
Do you want to exit [1(yes)/0(no)]: 1
```
## Assignment 4:
***
Create a class to represent a book with attributes and methods,; Implement inheritance by creating subclasses for different types of books,; Write a generator function to generate the Fibonacci series.
CODE:
```python
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def display(self):
        print(
            f"Name: {self.name}\nAuthor: {self.author}\nYear of Publication: {self.year}"
        )


class ScienceFiction(Book):
    def __init__(self, name, author, year, main_character):
        super().__init__(name, author, year)
        self.main_character = main_character

    def display(self):
        super().display()
        print(f"Main Character: {self.main_character}")


class Romance(Book):
    def __init__(self, name, author, year, main_plot):
        super().__init__(name, author, year)
        self.main_plot = main_plot

    def display(self):
        super().display()
        print(f"Main Plot: {self.main_plot}")


def Fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = Fibonacci()
limit = int(input("Enter no of terms of Fibonacci Series: "))
fib_series = []
for _ in range(limit):
    fib_series.append(next(fib_gen))
print(fib_series)
```
OUTPUT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment4.py
Enter no of terms of Fibonacci Series: 6
[0, 1, 1, 2, 3, 5]
```
## Assignment 5:
***
Use lambda function, map and filter to perform operations on a list,; Create a module that contains functions for mathematical operations,; Import and use functions from external packages (e.g. math, random).
CODE:
`main.py`:
```python
lst = [1, 2, 3, 45, 6, 3, 5, 23, 6, 5, 543, 76, 32, 75]
iseven = lambda x: True if x % 2 == 0 else False
square = lambda x: x * x
lstOfSquares = list(map(square, lst))
even_no = list(filter(iseven, lst))
print(lst)
print(f"Square of each number in the above list: {lstOfSquares}")
print(f"Even numbers in the above list: {even_no}")


import operations

print(operations.add(23, 4, 5, 346, 234))
print(operations.substract(29, 15))
print(operations.multiply(23, 45))
print(operations.divide(24, 6))

import math
import random

print("sin(30) =", math.sin(math.radians(30)))
print("abs(-34) =", math.fabs(-34))
print("These are 5 random integer between 1 and 100 (including both 1 and 100):")
for _ in range(5):
    print(random.randint(1, 100))
```
`operations.py`:
```python
def add(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


def multiply(x, y):
    return x * y


def substract(x, y):
    return x - y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Division by zero is not allowed!")
```
OUTPUT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment5.py
[1, 2, 3, 45, 6, 3, 5, 23, 6, 5, 543, 76, 32, 75]
Square of each number in the above list: [1, 4, 9, 2025, 36, 9, 25, 529, 36, 25, 294849, 5776, 1024, 5625]
Even numbers in the above list: [2, 6, 6, 76, 32]
612
14
1035
4.0
sin(30) = 0.49999999999999994
abs(-34) = 34.0
These are 5 random integer between 1 and 100 (including both 1 and 100):
66
27
4
74
31
```

## Assignment 6:
***
Create and manipulate NumPy arrays. Perform basic operations and indexing on arrays.
CODE:
```python
import numpy as np

# Array Creation and generation
print("Array Creation and generation: ")
array1D = np.array([2, 5, 7], dtype=np.uint32)
array2D = np.array([[2, 3, 5], [4, 6, 8], [4, 7, 3]])
array3D = np.array([[[3, 6, 3], [5, 7, 5]], [[4, 6, 3], [5, 7, 4]]])


print("1 dimensional array", array1D)
print("2 dimensional array", array2D)
print("3 dimensional array", array3D)

seq1 = np.arange(2, 3, 0.1)
seq2 = np.arange(10)

print("np.arange(2(start value), 3(end value), 0.1(step))", seq1)
print("np.arange(10(start value))", seq2)

arr = np.linspace(2, 3, 6)
print("np.linspace(2(start), 3(stop), 6(no of equidistance values))", arr)

arr2D = np.vander(np.linspace(0, 2, 5), 2)
print("np.vander(np.linspace(0, 2, 5), 2)", arr2D)

zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((2, 3, 2))

print("zeros array:", zeros_arr)
print("ones array:", ones_arr)

# INDEXING
print("Indexing: ")
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])

ar = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd dim: ", ar[1, -1])


# Manipulation
print("Manipulation: ")
x = np.arange(35)
print("x =", x)
y = x.reshape((7, 5))

print("x.reshape((7, 5))", y)

a = np.array([3, 2, 0, 1])

print("sorting", np.sort(a))

b = np.array(["banana", "cherry", "apple"])

print("sorting", np.sort(b))

print("Accessing elements using some condition")
z = np.array([41, 42, 43, 44])
condition = [True, False, True, False]

newarr = z[condition]
print("array", z)
print("condition", condition)
print("new array", newarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr1)
print(arr2)
print("Concatenation", arr3)

arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])
arr6 = np.concatenate((arr4, arr5), axis=1)
print(arr4)
print(arr5)
print("Concatenation", arr6)
```
OUTPUT:
```shell
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment6.py
Array Creation and generation:
1 dimensional array [2 5 7]
2 dimensional array [[2 3 5]
 [4 6 8]
 [4 7 3]]
3 dimensional array [[[3 6 3]
  [5 7 5]]

 [[4 6 3]
  [5 7 4]]]
np.arange(2(start value), 3(end value), 0.1(step)) [2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9]
np.arange(10(start value)) [0 1 2 3 4 5 6 7 8 9]
np.linspace(2(start), 3(stop), 6(no of equidistance values)) [2.  2.2 2.4 2.6 2.8 3. ]
np.vander(np.linspace(0, 2, 5), 2) [[0.  1. ]
 [0.5 1. ]
 [1.  1. ]
 [1.5 1. ]
 [2.  1. ]]
zeros array: [[0. 0. 0.]
 [0. 0. 0.]]
ones array: [[[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]]
Indexing:
[1 3 5]
Last element from 2nd dim:  10
Manipulation:
x = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34]
x.reshape((7, 5)) [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]
 [25 26 27 28 29]
 [30 31 32 33 34]]
sorting [0 1 2 3]
sorting ['apple' 'banana' 'cherry']
Accessing elements using some condition
array [41 42 43 44]
condition [True, False, True, False]
new array [41 43]
[1 2 3]
[4 5 6]
Concatenation [1 2 3 4 5 6]
[[1 2]
 [3 4]]
[[5 6]
 [7 8]]
Concatenation [[1 2 5 6]
 [3 4 7 8]]
```

## Assignment 7:
***
Implement string operations (e.g. Concatenation, slicing). Use regular expressions to validate email addresses.
CODE:
```python
# Concatenation
print("Concatenation: ")
first_name = "Yash"
last_name = "Sharma"

full_name = first_name + " " + last_name
print(full_name)

e = "e"
print("'e' * 3 =", e * 3)
print("'e' + 'e' =", e + e)
print()

# Slicing
print("Slicing: ")
string = "This is an example string"
print("string[start(default = 0):stop(not included):step(default = 1)]")
print("string[:4] =", string[:4])
print("string[2:9] =", string[2:9])
print("string[::2] =", string[::2])
print("string[4::3] =", string[4::3])
print("string[::-1] =", string[::-1])
print("string[::] =", string[::])
print()

# Splitting
print("Splitting: ")
string = "This is an example string"
l1 = string.split()
l2 = string.split("i")
print("string.split() =", l1)
print("string.split('i') =", l2)
print()

# Casing
print("Casing: ")
string = "tHis Is aN eXaMple sTRIng"
title_string = string.title()
upper_string = string.upper()
lower_string = string.lower()
swapcase_string = string.swapcase()
print("original string =", string)
print("string.title() =", title_string)
print("string.upper() =", upper_string)
print("string.lower() =", lower_string)
print("string.swapcase() =", swapcase_string)
print()

# Translation
print("Uses a dictionary with ascii codes to replace 83 (S) with 80 (P):")
mydict = {83: 80}
txt = "Hello Sam!"

print(txt, "----->", txt.translate(mydict))
print()


print("Regex: ")
import re


def validate_email(email):
    # Regular expression pattern for basic email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Compile the pattern
    regex = re.compile(pattern)
    # Match the email against the pattern
    if regex.match(email):
        return True
    else:
        return False


# Test the function
emails = [
    "example@example.com",
    "user.name@example.co.jp",
    "user@domain-with-dash.com",
    "user123@example123.co.uk",
    "invalid-email.com",
    "user@example.",
    "@example.com",
    "user@example",
    "user@.com",
]

for email in emails:
    print(f"{email}: {validate_email(email)}")
```
OUTPUT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment7.py
Concatenation:
Yash Sharma
'e' * 3 = eee
'e' + 'e' = ee

Slicing:
string[start(default = 0):stop(not included):step(default = 1)]
string[:4] = This
string[2:9] = is is a
string[::2] = Ti sa xml tig
string[4::3] =    alsi
string[::-1] = gnirts elpmaxe na si sihT
string[::] = This is an example string

Splitting:
string.split() = ['This', 'is', 'an', 'example', 'string']
string.split('i') = ['Th', 's ', 's an example str', 'ng']

Casing:
original string = tHis Is aN eXaMple sTRIng
string.title() = This Is An Example String
string.upper() = THIS IS AN EXAMPLE STRING
string.lower() = this is an example string
string.swapcase() = ThIS iS An ExAmPLE StriNG

Uses a dictionary with ascii codes to replace 83 (S) with 80 (P):
Hello Sam! -----> Hello Pam!

Regex:
example@example.com: True
user.name@example.co.jp: True
user@domain-with-dash.com: True
user123@example123.co.uk: True
invalid-email.com: False
user@example.: False
@example.com: False
user@example: False
user@.com: False
```
## Assignment 8:
***
Read data from a text file and perform operations. Handle exceptions for file operations and input validation.
CODE:
```python
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def operations(data):
    if data:
        try:
            data = [int(d) for d in data]
            total_sum = sum(num for num in data)
            average = total_sum / len(data)
            max_value = max(data)
            min_value = min(data)
            print(f"Total sum: {total_sum}")
            print(f"Average: {average}")
            print(f"Maximum value: {max_value}")
            print(f"Minimum value: {min_value}")
        except ValueError:
            print("Error: Invalid data in the file.")
    else:
        print("No data to perform operations.")


def main():

    file_path = input("Enter the path to the text file: ")
    try:
        data = read_file(file_path)
        if data:
            operations(data)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
OUTPUT:
```bash
(base) ➜  Computer-Programming git:(main) ✗ python3 assignment8.py
Enter the path to the text file: data.txt
Total sum: 6589
Average: 313.76190476190476
Maximum value: 764
Minimum value: 23
```
