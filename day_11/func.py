def add_two_numbers (a, b):
    sum = a + b
    return sum
print(add_two_numbers(5, 10))

def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area
print(area_of_circle(7))
    
def add_all_nums(*args):
    # Check if all arguments are numbers
    if not all(isinstance(arg, (int, float)) for arg in args):
        return "Error: All arguments must be numbers."
    
    return sum(args)

print(add_all_nums(1, 2, 3))       
print(add_all_nums(1, "two", 3))   
print(add_all_nums(1.5, 2.3, 3.2))  

def convert_celsius_to_fahrenheit(C):
    fahrenheit = (C * 9/5) + 32
    return fahrenheit

temp_in_celsius = 25
temp_in_fahrenheit = convert_celsius_to_fahrenheit(temp_in_celsius)
print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F")


def check_season(month):
    month = month.strip().lower()
    if month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    else:
        return "Error: Invalid month. Please provide a valid month name."
print(check_season("March"))
print(check_season("August"))
print(check_season("  January  "))
print(check_season("InvalidMonth"))  

def calculate_slope(x1, y1, x2, y2):
 
    slope = (y2 - y1) / (x2 - x1)
    return slope
    
print(calculate_slope(1, 2, 4, 6)) 

def solve_quadratic_eqn(a, b, c, x):
    eqn = a*x**2 + b*x + c
    return eqn
print(solve_quadratic_eqn(2,4,6,8))

def print_list(lst):
    for i in lst:
        print(i)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print_list(my_list)

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1): 
        reversed_arr.append(arr[i]) 
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5])) 
print(reverse_list(["A", "B", "C"])) 

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
print(capitalize_list_items(['a', 'b', 'c', 'd']))

def add_item(lst, itm):
    lst.append(itm)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5)) 

def remove_item(lst, itm):
    lst.remove(itm)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3)) 

def sum_of_numbers(nums):
    total = 0 
    for num in range(1, nums + 1): 
        total += num 
    return total 

print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

def sum_of_odds(nums):
    total = 0 
    for num in range(1, nums + 1):
        if num % 2 == 0:
            total += num 
    return total 

print(sum_of_odds(5)) 
print(sum_of_odds(10)) 
print(sum_of_odds(100))

def evens_and_odds(n):
    evens = 0  
    odds = 0   
    
    for num in range(1, n + 1):  
        if num % 2 == 0:  
            evens += 1
        else:  
            odds += 1
    
    return f"The number of odds are {odds}. The number of evens are {evens}."


print(evens_and_odds(100)) 

import statistics

# 1. Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
print(factorial(4))

# # 2. is_empty Function
def is_empty(param):
    return len(param) == 0

print(is_empty('Hello'))

# # 3. Statistical Functions for Lists
# 3.1 Calculate Mean
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0
print(calculate_mean([1, 2, 3, 4, 5]))

# 3.2 Calculate Median
def calculate_median(lst):
    return statistics.median(lst) if lst else 0 
print(calculate_median([1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]))

# # 3.3 Calculate Mode
def calculate_mode(lst):
    try:
        return statistics.mode(lst)
    except statistics.StatisticsError:
        return "No unique mode"
print(calculate_mode([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,3,4,2,4,6,3,2,4,4,2,1,2,5,1,3,1]))

# # 3.4 Calculate Range
def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0
print(calculate_range([1,1,2,2,3,4,5,2,1,5,6,8,9,2,5,5,3,5,2,1,6,7]))

# 3.5 Calculate Variance
def calculate_variance(lst):
    return statistics.variance(lst) if len(lst) > 1 else 0 
print(calculate_variance([10,20,30,40,50,60]))

# # 3.6 Calculate Standard Deviation
def calculate_std(lst):
    return statistics.stdev(lst) if len(lst) > 1 else 0  
print(calculate_std([50,60,70,80,90]))

import math

def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  
    return True  

print(is_prime(2))  
print(is_prime(3))  
print(is_prime(4))  
print(is_prime(18)) 

def are_all_items_unique(lst):
    return len(lst) == len(set(lst))

print(are_all_items_unique([1, 2, 3, 4]))  
print(are_all_items_unique([1, 2, 2, 4]))  
print(are_all_items_unique([10, 20, 30])) 
print(are_all_items_unique([5, 5, 5, 5])) 

def are_all_items_same_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)

print(are_all_items_same_type([1, 2, 3, 4]))   
print(are_all_items_same_type([1, 2.0, 3, 4]))       
print(are_all_items_same_type(["a", "b", "c"]))      
print(are_all_items_same_type([1, "2", 3, 4]))      

import keyword

def is_valid_python_variable(variable_name):
    return variable_name.isidentifier() and not keyword.iskeyword(variable_name)

print(is_valid_python_variable("valid_var")) 
print(is_valid_python_variable("1invalid"))  
print(is_valid_python_variable("def"))       
print(is_valid_python_variable("another_valid_var"))
