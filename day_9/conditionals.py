# Ask the user to enter their age
user = int(input("Enter your age: "))

# Check if the user is old enough to drive
if user >= 18:
    print("You are old enough to drive.")
elif user < 18:
    # If not, calculate how many more years they need to learn to drive
    age = 18 - user
    print(f"You need {age} more years to learn to drive.")
    
# Define my age
my_age = 22

# Get the user's age as input
your_age = int(input("Enter your age: "))

# Compare the ages and print the age difference
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"I am {age_difference} years older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"You are {age_difference} years older than me.")
    else:
        print(f"You are {age_difference} years older than me ")
else:
    print("We are the same age.")

# Ask for two numbers and compare them
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")

# Ask for a grade and print the corresponding letter grade
grade = int(input("Enter grades: "))
if grade >= 80 and grade <= 100:
    print("A")
elif grade >= 70 and grade <= 89:
    print("B")
elif grade >= 60 and grade <= 69:
    print("C")
elif grade >= 50 and grade <= 59:
    print("D")
elif grade >= 0 and grade <= 49:
    print("E")
else:
    print("F")

# Ask for a season and print the corresponding season in the year
season = input("Enter season: ")
if season == "September" or season == "October" or season == "November":
    print("The season is Autumn.")
elif season == "December" or season == "January" or season == "February":
    print("The season is Winter.")
elif season == "March" or season == "April" or season == "May":
    print("The season is Spring.")
elif season == "June" or season ==  "July " or season == "August":
    print("The season is Summer.")

# Ask for a missing fruit and check if it exists in the list of fruits
fruit = input("Enter missing fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit not in fruits:
    modified_list = fruits.append(fruit)
    print(f"Modified list is: {fruits}.")
elif fruit in fruits:
    print(f"That fruit already exists in the list.")
    
# Dictionary of person information
person = {
    'first_name': 'John',
    'last_name': 'Akech',
    'age': 22,
    'country': 'Rwanda',
    'is_married': False,
    'skills': ['Python', 'C', 'Java', 'SQL'],
    'address': {
        'street': 'Valley View Partment, Masoro',
        'zipcode': '00000'
    }
}

# Check if the person dictionary has the 'skills' key
if 'skills' in person:
    skills = person['skills']

    # Print out the middle skill in the skills list
    middle_index = len(skills) // 2
    print(f"The middle skill is: {skills[middle_index]}")

    # Check if the person has the 'Python' skill
    has_python = 'Python' in skills
    print(f"Does the person have Python skill? {'Yes' if has_python else 'No'}")

    # Determine the person's title based on their skills
    if skills == ['JavaScript', 'React']:
        print('He is a front end developer')
    elif set(['SQL', 'Python']).issubset(skills):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print('He is a fullstack developer')
    else:
        print('Unknown title')

# Check if the person is married and lives in Rwanda
if person['is_married'] and person['country'] == 'Rwanda':
    print(f"{person['first_name']} {person['last_name']} is married and lives in {person['country']}.")
else:
    print(f"{person['first_name']} {person['last_name']} is not married and lives in {person['country']}.")