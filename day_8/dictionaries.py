# Creating an empty dictionary for 'dog' and printing its type
dog = {}
print(type(dog))  # Output will be <class 'dict'> since 'dog' is a dictionary

# Defining a dictionary with attributes of a dog
dog = {
    'name': 'Wudut',
    'color': 'Yellow',
    'breed': 'African',
    'legs': 4,
    'age': 15
}

# Printing the dog dictionary
print(dog)

# Defining a dictionary with student details
student_dict = {
    'first_name': 'John',
    'last_name': 'Akech',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'Skills': ['Python', 'SQL', 'HTML', 'Java', 'C'],
    'country': 'South Sudan',
    'city': 'Juba',
    'address': {
        'street': 'Valley View Apartment, Masoro',
        'Zip_code': 00000
    }
}

# Printing the entire student dictionary
print(student_dict)

# Finding the length of the student dictionary (number of key-value pairs)
length = len(student_dict)
print(length)

# Printing the values of the dictionary
print(student_dict.values())

# Accessing and printing the 'Skills' list from the student dictionary
skills_values = (student_dict['Skills'])
print(f"skills_values: {skills_values}")

# Adding a new skill to the student's skills list
student_dict['Skills'].append('Flutter')

# Adding multiple skills to the skills list
student_dict['Skills'].extend(['Django', 'Machine Learning'])

# Printing the updated skills list
print(student_dict['Skills'])

# Printing the keys of the student dictionary
print(student_dict.keys())

# Printing the values function reference (not actual values)
print(student_dict.values)

# Converting the student dictionary keys to a list and a tuple
student_lst = list(student_dict)
student_tupl = tuple(student_dict)

# Printing the list and tuple of dictionary keys
print(f"The student list is: {student_lst}")
print(f"The student tuple is : {student_tupl}")

# Deleting the 'address' key from the student dictionary and the entire 'dog' dictionary
del(student_dict['address'])
del(dog)

# Printing the modified student dictionary (without 'address')
print(student_dict)