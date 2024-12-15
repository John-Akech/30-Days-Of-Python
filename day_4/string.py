# Joining a list into a string with a space separator
course = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(course))  # Output: 'Thirty Days Of Python'

# Joining a list into a string with a space separator and storing it in a variable
c = ['Coding', 'For', 'All']
joined_c = ' '.join(c)
print(joined_c)  # Output: 'Coding For All'

# Working with a string
company = 'SudoMind'
print(company)  # Output: 'SudoMind'

print(len(company))  # Output: 8 (length of the string)

# Converting the string to uppercase
print(company.upper())  # Output: 'SUDOMIND'

# Capitalizing, title-casing, and swapping case of the string
print(joined_c.capitalize())  # Output: 'Coding for all' (First letter of the string is capitalized)
print(joined_c.title())  # Output: 'Coding For All' (First letter of each word is capitalized)
print(joined_c.swapcase())  # Output: 'cODING fOR aLL' (Uppercase letters become lowercase and vice versa)

# Slicing the string
print(joined_c[0:6])  # Output: 'Coding' (First six characters)

# Checking if 'Coding' exists in the list c
print('Coding' in c)  # Output: True (because 'Coding' is in the list)

# Replacing 'Coding' with 'Python' in the string
print(joined_c.replace('Coding', 'Python'))  # Output: 'Python For All'

# Splitting a string by commas
social_media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(social_media.split(','))  # Output: ['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']

# Accessing specific characters of a string
print(joined_c[0])  # Output: 'C' (First character of the string)
print(joined_c[-1])  # Output: 'l' (Last character of the string)
print(joined_c[10])  # Output: 'l' (11th character of the string)

# Creating an acronym from a phrase
phrase = "Python For Everyone"
acronym = ''.join(word[0] for word in phrase.split()).upper()
print(acronym)  # Output: 'PFE'

# Creating an acronym from another phrase
phrase_2 = "Coding For All"
acronym_2 = ''.join(word[0] for word in phrase_2.split()).upper()
print(acronym_2)  # Output: 'CFA'

# Printing a formatted table with tabs
print("\t\tName\tAge\tCountry\tCity")
print("\t\tJohn\t100\tSSD\tJuba")