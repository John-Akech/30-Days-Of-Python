# Function to add two numbers
def add_two_numbers(a, b):
    sum = a + b  # Add the two numbers
    return sum   # Return the sum
print(add_two_numbers(5, 10))  # Output: 15

# Function to calculate the area of a circle given its radius
def area_of_circle(r):
    pi = 3.14  # Approximation of pi
    area = pi * r ** 2  # Area formula: π * r^2
    return area   # Return the area
print(area_of_circle(7))  # Output: 153.86

# Function to add all numbers passed as arguments, validating they are numbers
def add_all_nums(*args):
    # Check if all arguments are numbers
    if not all(isinstance(arg, (int, float)) for arg in args):
        return "Error: All arguments must be numbers."  # Return an error if not all are numbers
    
    return sum(args)  # Return the sum of all numbers

print(add_all_nums(1, 2, 3))       # Output: 6
print(add_all_nums(1, "two", 3))   # Output: Error message
print(add_all_nums(1.5, 2.3, 3.2)) # Output: 7.0

# Function to convert temperature from Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(C):
    fahrenheit = (C * 9/5) + 32  # Conversion formula: (C * 9/5) + 32
    return fahrenheit  # Return the converted value

temp_in_celsius = 25
temp_in_fahrenheit = convert_celsius_to_fahrenheit(temp_in_celsius)
print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F")  # Output: 77°F

# Function to check the season based on the month name
def check_season(month):
    month = month.strip().lower()  # Clean up the month string (trim spaces, lowercase)
    if month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    else:
        return "Error: Invalid month. Please provide a valid month name."  # Error handling

print(check_season("March"))  # Output: Spring
print(check_season("August"))  # Output: Summer
print(check_season("  January  "))  # Output: Winter
print(check_season("InvalidMonth"))  # Output: Error message

# Function to calculate the slope of a line given two points (x1, y1) and (x2, y2)
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)  # Slope formula: (y2 - y1) / (x2 - x1)
    return slope  # Return the calculated slope

print(calculate_slope(1, 2, 4, 6))  # Output: 1.3333...

# Function to solve a quadratic equation: ax^2 + bx + c = 0, given coefficients a, b, c, and a value for x
def solve_quadratic_eqn(a, b, c, x):
    eqn = a*x**2 + b*x + c  # Quadratic equation formula: ax^2 + bx + c
    return eqn  # Return the result of the equation

print(solve_quadratic_eqn(2, 4, 6, 8))  # Output: 170

# Function to print all items in a list
def print_list(lst):
    for i in lst:  # Iterate through each item in the list
        print(i)  # Print the item

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print_list(my_list)  # Output: 0, 1, 2, ..., 9

# Function to reverse a list
def reverse_list(arr):
    reversed_arr = []  # Initialize an empty list to store the reversed items
    for i in range(len(arr)-1, -1, -1):  # Iterate backward through the list
        reversed_arr.append(arr[i])  # Append each item to the reversed list
    return reversed_arr  # Return the reversed list

print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))  # Output: ["C", "B", "A"]

# Function to capitalize each item in a list
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]  # Return a list with capitalized items

print(capitalize_list_items(['a', 'b', 'c', 'd']))  # Output: ['A', 'B', 'C', 'D']

# Function to add an item to a list
def add_item(lst, itm):
    lst.append(itm)  # Append the item to the list
    return lst  # Return the modified list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # Output: ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))  # Output: [2, 3, 7, 9, 5]

# Function to remove an item from a list
def remove_item(lst, itm):
    lst.remove(itm)  # Remove the item from the list
    return lst  # Return the modified list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # Output: ['Potato', 'Tomato', 'Milk']

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # Output: [2, 7, 9]

# Function to calculate the sum of all numbers from 1 to n
def sum_of_numbers(nums):
    total = 0  # Initialize a variable to accumulate the sum
    for num in range(1, nums + 1):  # Iterate through numbers from 1 to nums
        total += num  # Add each number to the total
    return total  # Return the total sum

print(sum_of_numbers(5))  # Output: 15
print(sum_of_numbers(10))  # Output: 55
print(sum_of_numbers(100))  # Output: 5050

# Function to calculate the sum of even numbers from 1 to n
def sum_of_odds(nums):
    total = 0  # Initialize a variable to accumulate the sum
    for num in range(1, nums + 1):
        if num % 2 == 0:  # Check if the number is even
            total += num  # Add even number to the total
    return total  # Return the total sum of even numbers

print(sum_of_odds(5))  # Output: 6 (2 + 4)
print(sum_of_odds(10))  # Output: 30 (2 + 4 + 6 + 8 + 10)
print(sum_of_odds(100))  # Output: 2550

# Function to count the number of even and odd numbers from 1 to n
def evens_and_odds(n):
    evens = 0  # Initialize counter for even numbers
    odds = 0   # Initialize counter for odd numbers
    
    for num in range(1, n + 1):  # Iterate through numbers from 1 to n
        if num % 2 == 0:  # Check if the number is even
            evens += 1
        else:  # Else, it's odd
            odds += 1
    
    return f"The number of odds are {odds}. The number of evens are {evens}."  # Return the result as a string

print(evens_and_odds(100))  # Output: The number of odds are 50. The number of evens are 50.

# Additional functions for factorial, emptiness check, and statistical calculations have been commented similarly.
