# Create an empty list
emppty_list = []
print(emppty_list)  # Output: []
print(type(emppty_list))  # Output: <class 'list'>

# List of integers from 0 to 9
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(items)
print(items)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(length)  # Output: 10

# Accessing elements in the list
print(items[0])  # Output: 0
print(len(items) // 2)  # Output: 5 (index of the middle element)
print(items[-1])  # Output: 9 (last element)

# List with mixed data types
mixed_data_types = ['John', 22, 1.78, 'Single', "Kigali,Rwanda"]
print(mixed_data_types)  # Output: ['John', 22, 1.78, 'Single', 'Kigali,Rwanda']
print(type(mixed_data_types))  # Output: <class 'list'>

# List of companies
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies)  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# List operations
print(len(companies))  # Output: 7
print(companies[0])  # Output: 'Facebook'
print(len(companies) // 2)  # Output: 3 (middle index)
print(companies[-1])  # Output: 'Amazon'

# Modifying a list element
companies[5] = 'Instagram'
print(companies)  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Instagram', 'Amazon']

# Adding elements to the list
companies.append('Samsung')  # Adds 'Samsung' at the end
print(companies)  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Instagram', 'Amazon', 'Samsung']
companies.insert(4, 'Tesla')  # Inserts 'Tesla' at index 4
print(companies)  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'Tesla', 'IBM', 'Instagram', 'Amazon', 'Samsung']

# String manipulation
print(companies[0].upper())  # Output: 'FACEBOOK'

# Join list elements into a single string
result = '#; '.join(companies)
print(result)  # Output: 'Facebook#; Google#; Microsoft#; Apple#; Tesla#; IBM#; Instagram#; Amazon#; Samsung'

# Check if an element is in the list
print('Yego' in companies)  # Output: False (since 'Yego' is not in the list)

# Sorting the list
companies.sort()  # Sorts in ascending order
print(companies)  # Output: Sorted list in alphabetical order

companies.sort(reverse=True)  # Sorts in descending order
print(companies)  # Output: Sorted list in reverse alphabetical order

# Slicing the list
print(companies[:3])  # Output: The first three companies in the list
print(companies[::-3])  # Output: List with every third element in reverse order

# Finding the middle element
middle_index = (len(companies) // 2)
middle_company = companies[middle_index]
print(middle_company)  # Output: Middle company in the list

# Removing the first element from the list
companies.pop(0)  # Removes 'Facebook'
print(companies)  # Output: List without 'Facebook'

# Deleting middle elements (if list has an even number of elements)
middle_start = len(companies) // 2 - 1
middle_end = len(companies) // 2 + 1
del companies[middle_start:middle_end]
print(companies)  # Output: List after removing the middle elements