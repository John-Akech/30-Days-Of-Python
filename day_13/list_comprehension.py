# 1. Filter numbers less than or equal to zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# Using list comprehension to keep only numbers that are <= 0
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)  # Output: [-4, -3, -2, -1, 0]

# 2. Flatten a list of lists of lists into a single list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# Using nested list comprehensions to flatten the three-level nested list
flattened_list = [item for sublist in list_of_lists for inner_list in sublist for item in inner_list]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Create a list of tuples with powers of numbers
list_of_tuples = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
# List comprehension to generate tuples where each tuple consists of:
# (x, 1, x, x^2, x^3, x^4, x^5) for each x in the range 0 to 10
print(list_of_tuples)

# 4. Create a list of lists with country names and cities formatted in uppercase
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# List comprehension to format each country name and city:
# - Country name in uppercase
# - First 3 letters of the country name in uppercase
# - City name in uppercase
output = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(output)  # Output: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# 5. Create a list of dictionaries with country and city information
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# List comprehension to create a dictionary for each country, where:
# - 'country' key holds the country name in uppercase
# - 'city' key holds the city name in uppercase
output = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(output)  # Output: [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]

# 6. Create a list of concatenated names
names = [[('Asabeneh', 'Yetayeh')], [('John', 'Akech')], [('Donald', 'Trump')], [('Bill', 'Gates')], [('Elon', 'Musk')]]
# List comprehension to concatenate first and last names
output = [f'{name[0][0]} {name[0][1]}' for name in names]
print(output)  # Output: ['Asabeneh Yetayeh', 'John Akech', 'Donald Trump', 'Bill Gates', 'Elon Musk']

# 7. Lambda function to calculate slope and y-intercept of a line given two points
calculate_line = lambda x1, y1, x2, y2: ( (y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1 )
# Example usage to calculate slope and y-intercept
x1, y1 = 1, 2
x2, y2 = 3, 4
# Calling the lambda function to get slope and intercept
slope, intercept = calculate_line(x1, y1, x2, y2)
print(f"Slope: {slope}, Y-intercept: {intercept}")  # Output: Slope: 1.0, Y-intercept: 1.0