# List of countries
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpacking
*nordic_countries, es, ru = names[:5] + names[5:]  # Split and unpack the list

# Display the results
print("Nordic Countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)