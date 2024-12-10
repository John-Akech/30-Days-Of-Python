age = 22
height = 1.79
com_num = 3+4j
base = input("Enter base: ")
height = input("Enter height: ")
area = 0.5 * int(base) * int(height)

print(f"The area of the triangle is {area:.0f}")

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print(f"The area of rectangle is {area}")
perimeter = 2 * (length + width)
print(f"The perimeter of rectangle is {perimeter}")

r = int(input("Enter the radius: "))
pi = 3.14
area = pi * r * r
print(f"The area of circle is {area}")
circumference = 2 * pi * r
print(f"The circumference of circle is {circumference}")


slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope

# Print the results
print(f"Slope: {slope}")
print(f"X-Intercept: {x_intercept}")
print(f"Y-Intercept: {y_intercept}")

import math

x1 = 2
x2 = 6
y1 = 2
y2 = 10

m = (y2-y1)/(x2-x1)
print(f"The slope is {m}")
d = math.sqrt((x2 - x2)**2 + (y2 - y1)**2)
print(f"The ecludian distatnt is {d}")

length_py = len("python")
length_dra = len("dragon")

if length_py == length_dra:
    print("The length of python equals the length of dragon")
elif length_py < length_dra:
    print("The length of python is less than the one of dragon")
elif length_py > length_dra:
    print("The length of python is greater that the length of dragon")
else:
    print("The there is no comparison")
    
print("on" in "python" and "dragon")

sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)
print(not "on", "dragon" and "python")

text = "python"
length = len(text)
flt = float(length)
string = str(length)

num = 4
even_num = num % 2 == 0
print(even_num)

print(7//3 == 2.7)

print(type("10") == type(10))

# print(int('9.8') == 10)

hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
earning = hours * rate_per_hour

print(f"Your weekly earning is {earning}")

# Constants
MAX_LIFESPAN_YEARS = 100  # Maximum lifespan in years
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # Days * Hours * Minutes * Seconds

# Prompt the user for the number of years
try:
    years = int(input("Enter the number of years: "))
    if years < 0:
        print("Please enter a positive number of years.")
    elif years > MAX_LIFESPAN_YEARS:
        print(f"A person can live a maximum of {MAX_LIFESPAN_YEARS} years.")
    else:
        # Calculate the number of seconds
        seconds_lived = years * SECONDS_IN_A_YEAR
        print(f"A person can live approximately {seconds_lived} seconds in {years} years.")
except ValueError:
    print("Please enter a valid integer for the number of years.")

# Loop to generate the rows of the table
for num in range(1, 6):
    print(f"{num} 1 {num} {num**2} {num**3}")
