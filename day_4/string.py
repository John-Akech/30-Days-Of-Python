course = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(course))

c = ['Coding', 'For' , 'All']
joined_c = ' '.join(c)
print(joined_c)

company = 'SudoMind'
print(company)

print(len(company))

print(company.upper())

print(joined_c.capitalize())
print(joined_c.title())
print(joined_c.swapcase())
print(joined_c[0:6])
print('Coding' in c)
print(joined_c.replace('Coding', 'Python'))
print(joined_c.split())
social_media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(social_media.split(','))
print(joined_c[0])
print(joined_c[-1])
print(joined_c[10])

phrase = "Python For Everyone"
acronym = ''.join(word[0] for word in phrase.split()).upper()
print(acronym)

phrase_2 = "Coding For All"
acronym_2 = ''.join(word[0] for word in phrase_2.split()).upper()
print(acronym_2)

print("\t\tName\tAge\tCountry\tCity")
print("\t\tJohn\t100\tSSD\tJuba")