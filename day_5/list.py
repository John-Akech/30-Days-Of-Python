emppty_list = []
print(emppty_list)
print(type(emppty_list))

items = [0,1,2,3,4,5,6,7,8,9]
length = len(items)
print(items)
print(length)

print(items[0])
print(len(items) // 2)
print(items[-1])

mixed_data_types = ['John',22,1.78,'Single',"Kigali,Rwanda"]
print(mixed_data_types)
print(type(mixed_data_types))

companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(companies)

print(len(companies))
print(companies[0])
print(len(companies)//2)
print(companies[-1])

companies[5] = 'Instagram'
print(companies)

companies.append('Samsung')
print(companies)
companies.insert(4, 'Tesla')
print(companies)

print(companies[0].upper())

result = '#; '.join(companies)
print(result)

print('Yego' in companies)

companies.sort()
print(companies)

companies.sort(reverse=True)
print(companies)

print(companies[:3])
print(companies[::-3])

middle_index = (len(companies)//2)
middle_company = companies[middle_index]
print(middle_company)

companies.pop(0)
print(companies)

middle_start = len(companies) // 2 - 1
middle_end = len(companies) // 2 + 1
del companies[middle_start:middle_end]

print(companies)