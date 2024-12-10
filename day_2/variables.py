# 'Day 2: 30 Days of python programming'
# Declare variables
first_name = "John"
last_name = "Akech"
full_name = "John Akech"
country = "South Sudan"
city = "Juba"
age = 22
year = 2024
is_married = False
is_true = True
is_light_on = False
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = "John", "Akech", "John Akech", "South Sudan", "Juba", 22, 2024, False, True, False

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)

# Check the data type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
# type(first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on)

print(len(first_name))
first_name = "John"
last_name = "Akech"

# Calculate the lengths
first_name_length = len(first_name)
last_name_length = len(last_name)

# Compare the lengths
if first_name_length > last_name_length:
    print("The first name is longer than the last name.")
elif first_name_length < last_name_length:
    print("The last name is longer than the first name.")
else:
    print("The first name and last name are of the same length.")


num_one = 5
num_two = 4
num_add = num_one + num_two
print(num_add)

num_sub = num_one - num_two
print(num_sub)

num_mul = num_one * num_two
print(num_mul)

num_div = num_one / num_two
print(num_div
      )
exp = pow(num_one, num_two)
print(exp)

floor_division = num_one // num_two
print(floor_division)

r = 30
area_of_circle = 3.14 * (r**2)
print(area_of_circle)

circum_of_circle = 2*3.14*r
print(circum_of_circle)

radius = int(input("What is the radius? "))
area = 3.14 * radius **2
print(area)

first_name1 = input("What is your first name? ")
print(first_name1)

last_name1 = input("What is your last name? ")
print(last_name1)

country1 = input("What country are you from? ")
print(country1)

age1= input("Enter your age ")
print(age1)