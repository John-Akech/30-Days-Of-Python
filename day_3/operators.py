# Assign initial values for age, height, and a complex number
age = 22
height = 1.79
com_num = 3 + 4j  # A complex number (real part 3, imaginary part 4)

# Get base and height for the triangle from the user and calculate area
base = input("Enter base: ")
height = input("Enter height: ")
area = 0.5 * int(base) * int(height)  # Area of a triangle formula (1/2 * base * height)

# Print the area of the triangle, rounded to 0 decimal places
print(f"The area of the triangle is {area:.0f}")

# Get the sides of the triangle from the user and calculate perimeter
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c  # Perimeter of a triangle formula (sum of sides)

# Print the perimeter of the triangle
print(f"The perimeter of the triangle is {perimeter}")

# Get the length and width of a rectangle from the user and calculate area and perimeter
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width  # Area of a rectangle formula (length * width)

# Print the area of the rectangle
print(f"The area of rectangle is {area}")
# Calculate and print the perimeter of the rectangle
perimeter = 2 * (length + width)  # Perimeter of a rectangle formula (2 * (length + width))
print(f"The perimeter of rectangle is {perimeter}")

# Get the radius of a circle and calculate area and circumference
r = int(input("Enter the radius: "))
pi = 3.14  # Approximate value of pi
area = pi * r * r  # Area of a circle formula (π * radius^2)

# Print the area of the circle
print(f"The area of circle is {area}")
# Calculate and print the circumference of the circle
circumference = 2 * pi * r  # Circumference of a circle formula (2 * π * radius)
print(f"The circumference of circle is {circumference}")

# Example of a line equation y = mx + b; calculating the x-intercept for the given slope and y-intercept
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope  # Formula for x-intercept when y = 0

# Print the slope, x-intercept, and y-intercept values
print(f"Slope: {slope}")
print(f"X-Intercept: {x_intercept}")
print(f"Y-Intercept: {y_intercept}")

# Calculate the slope and Euclidean distance between two points (x1, y1) and (x2, y2)
import math
x1 = 2
x2 = 6
y1 = 2
y2 = 10

m = (y2 - y1) / (x2 - x1)  # Formula for slope (rise / run)
print(f"The slope is {m}")
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Euclidean distance formula (sqrt((x2 - x1)^2 + (y2 - y1)^2))
print(f"The Euclidean distance is {d}")

# Compare the lengths of the strings "python" and "dragon"
length_py = len("python")
length_dra = len("dragon")

# Check and print the comparison between the two lengths
if length_py == length_dra:
    print("The length of python equals the length of dragon")
elif length_py < length_dra:
    print("The length of python is less than the one of dragon")
elif length_py > length_dra:
    print("The length of python is greater than the length of dragon")
else:
    print("There is no comparison")

# Check if the substring "on" exists in both "python" and "dragon"
print("on" in "python" and "on" in "dragon")

# Check if the word "jargon" is in the sentence
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

# Check logical operations
print(not "on", "dragon" and "python")

# Convert string "python" to various data types and print the results
text = "python"
length = len(text)
flt = float(length)  # Convert length of the string to float
string = str(length)  # Convert length of the string to string

# Check if a number is even
num = 4
even_num = num % 2 == 0  # Check if the number is divisible by 2
print(even_num)

# Check the result of integer division
print(7 // 3 == 2.7)

# Check the data type of "10" and 10
print(type("10") == type(10))

# Prompt user for hours worked and rate per hour, then calculate weekly earnings
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
earning = hours * rate_per_hour  # Weekly earnings calculation

# Print the weekly earnings
print(f"Your weekly earning is {earning}")

# Constants for calculating the lifespan in seconds
MAX_LIFESPAN_YEARS = 100  # Maximum lifespan in years
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # Number of seconds in one year

# Prompt the user for the number of years and calculate the seconds
try:
    years = int(input("Enter the number of years: "))
    if years < 0:
        print("Please enter a positive number of years.")
    elif years > MAX_LIFESPAN_YEARS:
        print(f"A person can live a maximum of {MAX_LIFESPAN_YEARS} years.")
    else:
        # Calculate the number of seconds lived
        seconds_lived = years * SECONDS_IN_A_YEAR
        print(f"A person can live approximately {seconds_lived} seconds in {years} years.")
except ValueError:
    print("Please enter a valid integer for the number of years.")

# Loop to generate the rows of a table with numbers, squares, and cubes
for num in range(1, 6):
    print(f"{num} 1 {num} {num**2} {num**3}")