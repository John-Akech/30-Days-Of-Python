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