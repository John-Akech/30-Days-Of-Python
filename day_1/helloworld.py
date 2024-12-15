# Performing basic arithmetic operations
print(3 + 4)  # Addition of 3 and 4
print(4 - 3)  # Subtraction: 4 minus 3
print(3 * 4)  # Multiplication: 3 multiplied by 4
print(4 % 3)  # Modulus: remainder when 4 is divided by 3
print(4 / 3)  # Division: 4 divided by 3 (returns a float)
print(3 ** 4)  # Exponentiation: 3 raised to the power of 4
print(4 // 3)  # Floor division: 4 divided by 3 and rounded down to the nearest integer

# Printing string values (name, country, and statement)
print('John')  # Print first name
print('Akech')  # Print last name
print('South Sudan')  # Print country name
print('I am enjoying 30 days of python')  # Print statement

# Checking the data types of different values
print(type(10))  # Type of integer 10
print(type(9.8))  # Type of float 9.8
print(type(3.14))  # Type of float 3.14
print(type(4 - 4j))  # Type of complex number 4 - 4j
print(type(['AROMA', 'Python', 'South Sudan']))  # Type of list
print(type('John'))  # Type of string 'John'
print(type('Akech'))  # Type of string 'Akech'
print(type('South Sudan'))  # Type of string 'South Sudan'

# Example for different Python data types

## Numbers:

# Integer: Showing different integer types (positive, negative, zero)
print(type(-3))  # Negative integer
print(type(0))   # Zero integer
print(type(3))   # Positive integer

# Float: Floating-point number
print(3.14)  # Example of a float

# Complex: Complex number with real and imaginary parts
print(type(3 + 4j))  # Type of complex number

## String: Showing string type
print(type('John'))  # Type of string 'John'

# Boolean: Boolean values (True or False)
is_python_fun1 = True  # True boolean value
is_python_fun2 = False  # False boolean value
print(type(is_python_fun1))  # Type of is_python_fun1 (True)
print(type(is_python_fun2))  # Type of is_python_fun2 (False)

# List: A collection of items that can be changed (mutable)
lst = [1, 2, 3, 'Aroma']  # List with integers and a string
print(type(lst))  # Type of lst (list)

# Tuple: An ordered collection of items that cannot be changed (immutable)
tpl = (1, 2, 3, 4, 5)  # Tuple of integers
print(type(tpl))  # Type of tpl (tuple)

# Set: A collection of unique items
st1 = {1, 2, 3, 4}  # Set of integers
st2 = {2, 3, 4, 5}  # Another set of integers

# Set operations: union and intersection
st3 = st1.union(st2)  # Union of st1 and st2 (all unique elements)
st4 = st1.intersection(st2)  # Intersection of st1 and st2 (common elements)
print(type(st4))  # Type of st4 (set)

# Dictionary: A collection of key-value pairs
dict = {'name': "Aroma", "Age": "22"}  # Dictionary with keys 'name' and 'Age'
print(type(dict))  # Type of dict (dictionary)

# Euclidean distance calculation between two points (x1, y1) and (x2, y2)
import math  # Importing the math module for mathematical operations
x1 = 2  # x-coordinate of the first point
x2 = 10  # x-coordinate of the second point
y1 = 3  # y-coordinate of the first point
y2 = 8  # y-coordinate of the second point

# Calculating the Euclidean distance using the formula
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # sqrt((x2 - x1)^2 + (y2 - y1)^2)

print(d)  # Printing the Euclidean distance
print(type(d))  # Printing the type of d (should be a float)