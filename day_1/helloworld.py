print(3+4)
print(4-3)
print(3*4)
print(4%3)
print(4/3)
print(3**4)
print(4//3)

print('John')
print('Akech')
print('South Sudan')
print('I am enjoying 30 days of python')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['AROMA', 'Python', 'South Sudan']))
print(type('John'))
print(type('Akech'))
print(type('South Sudan'))

# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

## Numbers:
# Integer
print(type(-3))   # Negative
print(type(0))      # Zero
print(type(3))      # Positive

# Float
print(3.14)

# Complex
print(type(3+4j))

## String
print(type('John'))

# Boolean
is_python_fun1 = True
is_python_fun2 = False
print(type(is_python_fun1))
print(type(is_python_fun2))

# List
lst = [1,2,3,'Aroma']
print(type(lst))

# Tuple
tpl = (1,2,3,4,5)
print(type(tpl))

# Set
st1 = {1,2,3,4}
st2 = {2,3,4,5}

st3 = st1.union(st2)
st4 = st1.intersection(st2)
print(type(st4))

# Dictionary
dict = {'name': "Aroma", "Age": "22"}
print(type(dict))

# Euclidian distance
import math
x1 = 2
x2 = 10
y1 = 3
y2 = 8

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(d)
print(type(d))