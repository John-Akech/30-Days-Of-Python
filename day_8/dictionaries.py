dog = {}
print(type(dog))

dog = {
    'name': 'Wudut',
    'color': 'Yellow',
    'breed': 'African',
    'legs': 4,
    'age': 15
}

print(dog)

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

print(student_dict)
length = len(student_dict)
print(length)

print(student_dict.values())

skills_values = (student_dict['Skills'])
print(f"skills_values: {skills_values}")

# Adding a single skill
student_dict['Skills'].append('Flutter')

# Adding multiple skills
student_dict['Skills'].extend(['Django', 'Machine Learning'])

# Print the updated dictionary
print(student_dict['Skills'])

print(student_dict.keys())
print(student_dict.values)

student_lst = list(student_dict)
student_tupl = tuple(student_dict)
print(f"The student list is: {student_lst}")
print(f"The student tuple is : {student_tupl}")

del(student_dict['address'])
del(dog)

print(student_dict)