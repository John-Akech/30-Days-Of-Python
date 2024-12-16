# def generate_full_name ():
#     first_name = 'John'
#     last_name = 'Akech'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print(generate_full_name ())

# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     return total
# print(add_two_numbers())

# def greetings (name):
#     message = name + ', welcome to Python for Everyone!'
#     return message

# print(greetings('John'))

# def add_ten(num):
#     ten = 10
#     return num + ten
# print(add_ten(90))

# def square_number(x):
#     return x * x
# print(square_number(2))

# def area_of_circle (r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(10))

# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     print(total)
# print(sum_of_numbers(10))
# print(sum_of_numbers(100)) 

# def generate_full_name (first_name, last_name):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

# def sum_two_numbers (num_one, num_two):
#     sum = num_one + num_two
#     return sum
# print('Sum of two numbers: ', sum_two_numbers(1, 9))

# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age;

# print('Age: ', calculate_age(2024, 1997))

# def weight_of_object (mass, gravity):
#     weight = str(mass * gravity)+ ' N'
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# def print_fullname(firstname, lastname):
#     space = ' '
#     full_name = firstname  + space + lastname
#     print(full_name)
# print_fullname(firstname = 'John', lastname = 'Akech')

# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(num2 = 3, num1 = 2))

# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(2, 3))

# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age;
# print('Age: ', calculate_age(2019, 1819))

# def greetings (name = 'Peter'):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings())
# print(greetings('John'))

# def generate_full_name (first_name = 'Ajook', last_name = 'Abuoi'):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name

# print(generate_full_name())
# print(generate_full_name('John','Akech'))

# def calculate_age (birth_year,current_year = 2024):
#     age = current_year - birth_year
#     return age;
# print('Age: ', calculate_age(1997))

# def weight_of_object (mass, gravity = 9.81):
#     weight = str(mass * gravity)+ ' N'
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100)) 
# print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))

# def sum_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num 
#     return total
# print(sum_all_nums(2, 3, 5))

# def generate_groups (team,*args):
#     print(team)
#     for i in args:
#         print(i)
# generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

#You can pass functions around as parameters
# def square_number (n):
#     return n * n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3))


# import the module
# import os
# Creating a directory
# os.mkdir('my_dir')
# Changing the current directory
# os.chdir('path')
# Getting current working directory
# os.getcwd()
# Removing directory
# os.rmdir()

# import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
#print('Welcome {} {} {} {} {}. Enjoy your {} challenge!'.format(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]))

# to exit sys
# sys.exit()
# To know the largest integer variable it takes
# sys.maxsize
# To know environment path
# sys.path
# To know the version of python you are using
# sys.version

# from statistics import *

# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

# print(f"The mean age is {mean(ages):.2f}")
# print(f"The median age is {median(ages)}")
# print(f"The mode of ages is {mode(ages)}")
# print(f"The variance of ages is {variance(ages):.2f}")
# print(f"The standard deviation of ages is {stdev(ages):.2f}")

#import math
# print(f'The pi is: {math.pi:.2f}')
# print(f'The square root of 4 is: {math.sqrt(4):.0f}')
# print(f'The power of 3 is: {math.pow(2, 3):.0f}')
# print(f'The floor division of 9.81 is: {math.floor(9.81):.0f}')
# print(f'The ceil of 9.8 is: {math.ceil(9.81):.0f}')
# print(f'The log10 of 100 is: {math.log10(100):.0f}')


# Define two points in 2D space
# point1 = (1, 2)
# point2 = (4, 6)

# Calculate the Euclidean distance between the two points
# distance = dist(point1, point2)

# print(f"The Euclidean distance between {point1} and {point2} is {distance:.0f}")

# help(math)
#dir(math)

# import string
# print(f'The ASCII LETTERS ARE: {string.ascii_letters}')
# print(f'The digits are: {string.digits}')
# print(f'The special charactiers called punctuations are: {string.punctuation}')

# from random import random, randint
# print(random)
# print(randint(5, 20))

# language = 'Python'
# lst = list(language)
# print(type(lst))
# print(lst)

# lst = [i for i in language]
# print(type(lst))
# print(lst)

# numbers = [i for i in range(10)]
# print(numbers)

# squares = [i * i for i in range(11)]
# print(squares)

# numbers = [(i, i * i) for i in range(11)]
# print(numbers)

# x = lambda a, b: a + b
# print(x(1,2))

# square = lambda x: x ** 2
# print(square(3))

# cube = lambda x: x ** 3
# print(cube(3))

# def power(x):
#     return lambda n:x ** n
# cube = power(2)(3)
# print(cube)

# two_power_of_five = power(2)(5)
# print(two_power_of_five)

## Function as a Parameter
# def sum_numbers(nums):
#     return sum(nums)

# def higher_order_function(f, lst):
#     summation = f(lst)
#     return summation
# result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)

## Function as a Return Value
# def square(x):
#     return x ** 2

# def cube(x):
#     return x ** 3

# def absolute(x):
#     if x >= 0:
#         return x
#     else:
#         return -(x)

# def highrt_order_function(type):
#     if type == 'square':
#         return square
    
#     elif type == 'cube':
#         return cube
    
#     elif type == 'absolute':
#         return absolute
    
# result = highrt_order_function('square')
# print(result(3))
# result = highrt_order_function('cube')
# print(result(3))
# result = highrt_order_function('absolute')
# print(result(-3))

def subt():
    subt = 10
    def sub(num):
        return  num - subt
    return sub
closure = subt()
print(closure(20))
print(closure(15)) 