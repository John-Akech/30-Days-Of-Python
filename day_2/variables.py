# 'Day 2: 30 Days of Python programming'

# Declare variables to store user information
first_name = "John"  # First name of the person
last_name = "Akech"  # Last name of the person
full_name = "John Akech"  # Full name combining first and last name
country = "South Sudan"  # Country of origin
city = "Juba"  # City of residence
age = 22  # Age of the person
year = 2024  # The current year
is_married = False  # Marital status (not married)
is_true = True  # Boolean variable set to True
is_light_on = False  # Light status (light is off)

# Reassign values to variables
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = "John", "Akech", "John Akech", "South Sudan", "Juba", 22, 2024, False, True, False

# Printing the values of the variables
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

# Checking and printing the data types of the variables
print(type(first_name))  # Data type of first_name
print(type(last_name))   # Data type of last_name
print(type(full_name))   # Data type of full_name
print(type(country))     # Data type of country
print(type(city))        # Data type of city
print(type(age))         # Data type of age
print(type(year))        # Data type of year
print(type(is_married))  # Data type of is_married
print(type(is_true))     # Data type of is_true
print(type(is_light_on)) # Data type of is_light_on

# Checking the length of first_name
print(len(first_name))   # Length of first name

# Reassign first and last names
first_name = "John"
last_name = "Akech"

# Calculate the lengths of first and last names
first_name_length = len(first_name)
last_name_length = len(last_name)

# Compare the lengths of the first and last names
if first_name_length > last_name_length:
    print("The first name is longer than the last name.")
elif first_name_length < last_name_length:
    print("The last name is longer than the first name.")
else:
    print("The first name and last name are of the same length.")

# Perform basic arithmetic operations
num_one = 5  # First number for calculations
num_two = 4  # Second number for calculations

num_add = num_one + num_two  # Addition of the two numbers
print(num_add)  # Print the sum

num_sub = num_one - num_two  # Subtraction of the two numbers
print(num_sub)  # Print the result

num_mul = num_one * num_two  # Multiplication of the two numbers
print(num_mul)  # Print the product

num_div = num_one / num_two  # Division of the two numbers
print(num_div)  # Print the quotient

# Exponentiation: num_one raised to the power of num_two
exp = pow(num_one, num_two)
print(exp)  # Print the result of exponentiation

# Floor division: the result of division rounded down
floor_division = num_one // num_two
print(floor_division)  # Print the result of floor division

# Calculate the area of a circle using radius
r = 30  # Radius of the circle
area_of_circle = 3.14 * (r**2)  # Formula for area of circle: π * r^2
print(area_of_circle)  # Print the area

# Calculate the circumference of a circle
circum_of_circle = 2 * 3.14 * r  # Formula for circumference: 2 * π * r
print(circum_of_circle)  # Print the circumference

# User input for radius and calculation of area
radius = int(input("What is the radius? "))  # Get the radius from the user
area = 3.14 * radius ** 2  # Calculate the area using the input radius
print(area)  # Print the area

# Prompt user for their first name, and print it
first_name1 = input("What is your first name? ")
print(first_name1)

# Prompt user for their last name, and print it
last_name1 = input("What is your last name? ")
print(last_name1)

# Prompt user for their country, and print it
country1 = input("What country are you from? ")
print(country1)

# Prompt user for their age, and print it
age1 = input("Enter your age ")
print(age1)