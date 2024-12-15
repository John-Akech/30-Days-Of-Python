# Looping through a range of numbers from 0 to 9 and printing each number
for i in range(10):
    print(i)

# Initializing a variable and using a while loop to print numbers from 0 to 9
number = 0
while number < 10:
    print(number)
    number += 1

# Looping through a range of numbers from 10 to 0 (inclusive) in reverse and printing each number
for i in range(10, -1, -1):
    print(i)

# Initializing a variable and using a while loop to print numbers from 10 to 0 in reverse
num = 10
while num >= 0:
    print(num)
    num -= 1

# Loop to print increasing number of '#' symbols in each line
for i in range(1, 8):
    print("#" * i)

# Nested loop to print a grid of '#' symbols (8 rows and 8 columns)
for i in range(8): 
    for i in range(8):
        print('#', end=' ')  # Using 'end' to avoid starting a new line
    print()  # Print a new line after each row

# Loop to print the multiplication table for numbers 0 to 10
for i in range(11):
    print(f"{i} x {i} = {i * i}") 

# Loop to print each item in the list 'skills_lst'
skills_lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for skill in skills_lst:
    print(skill)

# Loop to print even numbers from 0 to 99
for i in range(100):
    if i % 2 == 0:
        print(i)

# Loop to print odd numbers from 0 to 99
for i in range(100):
    if i % 2 != 0:
        print(i)

# Loop to calculate the sum of all numbers from 0 to 100
total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers is {total_sum}")

# Loop to calculate the sum of all even numbers from 0 to 100
total_sum = 0
for i in range(101):
    if i % 2 == 0:
        total_sum += i
print(f"The sum of all even numbers is {total_sum}")

# Loop to calculate the sum of all odd numbers from 0 to 100
total_sum = 0
for i in range(101):
    if i % 2 != 0:
        total_sum += i
print(f"The sum of all odd numbers is {total_sum}")

# Loop through a list of countries and print those that contain 'land' in their name
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 
             'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 
             'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 
             'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 
             'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo', 
             'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 
             'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 
             'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 
             'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 
             'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 
             'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 
             'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 
             'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 
             'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 
             'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 
             'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 
             'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 
             'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 
             'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 
             'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 
             'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 
             'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 
             'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 
             'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 
             'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

for country in countries:
    if 'land' in country.lower():  # Checking if 'land' exists in the country name
        print(country)

# Reversing the order of items in a list and printing the result
lst = ['banana', 'orange', 'mango', 'lemon']
lst.reverse()  # Reversing the list
print(lst)