person = {
    'First_name': 'John',
    'Last_name': 'Akech',
    'COuntry': 'South Sudan',
    'City': 'Juba',
    'Skills': ['Python', 'SQL', 'Java'],
    'Address': {
        'Street': 'Masoro',
        'Zip code': 00000
    }
}

print(person.get('First_name'))
print(person.get('Last_name'))
print(person.get('Country'))
print(person.get('City'))
print(person.get('Skills'))
print(person.get('Skills')[0])
print(person.get('Address'))

print(person.items())
print(person.keys())
print(person.values())