# Create an empty tuple
empty_tpl = tuple()
print(empty_tpl)  # Output: ()

# Create a tuple with names of siblings
names_of_siblings = ('Kuot', 'Abuk', 'Adhieu', 'Awel')
print(names_of_siblings)  # Output: ('Kuot', 'Abuk', 'Adhieu', 'Awel')

# Create tuples for brothers and sisters
brothers_tuple = ('Deng', 'Kuot')
print(brothers_tuple)  # Output: ('Deng', 'Kuot')

sisters_tuple = ('Abuk', 'Adhieu', 'Awel')
print(sisters_tuple)  # Output: ('Abuk', 'Adhieu', 'Awel')

# Concatenate the brothers and sisters tuples to form the siblings tuple
siblings_tpl = brothers_tuple + sisters_tuple
print(siblings_tpl)  # Output: ('Deng', 'Kuot', 'Abuk', 'Adhieu', 'Awel')

# Create a tuple for parents and add it to the family members tuple
parents = ('Father', 'Mother')
family_members = siblings_tpl + parents
print(family_members)  # Output: ('Deng', 'Kuot', 'Abuk', 'Adhieu', 'Awel', 'Father', 'Mother')

# Slice the family_members tuple to get the first 5 elements as siblings
siblings = family_members[:5]
print(f"siblings: {siblings}")  # Output: siblings: ('Deng', 'Kuot', 'Abuk', 'Adhieu', 'Awel')

# Slice the family_members tuple from index 5 onwards to get the parents
parent = family_members[5:]
print(f"parents: {parent}")  # Output: parents: ('Father', 'Mother')

# Create tuples for fruits, vegetables, and animal products
fruits = ('Apple', 'Banana', 'Cherry', 'Mango')
print(fruits)  # Output: ('Apple', 'Banana', 'Cherry', 'Mango')

vegetables = ('Cabbage', 'Egg plant', 'Irish potatoes')
print(vegetables)  # Output: ('Cabbage', 'Egg plant', 'Irish potatoes')

animal_products = ('Milk', 'Meat', 'Butter', 'Cheese', 'Egg')
print(animal_products)  # Output: ('Milk', 'Meat', 'Butter', 'Cheese', 'Egg')

# Concatenate the food items into one tuple
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)  # Output: ('Apple', 'Banana', 'Cherry', 'Mango', 'Cabbage', 'Egg plant', 'Irish potatoes', 'Milk', 'Meat', 'Butter', 'Cheese', 'Egg')

# Convert the tuple to a list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)  # Output: ['Apple', 'Banana', 'Cherry', 'Mango', 'Cabbage', 'Egg plant', 'Irish potatoes', 'Milk', 'Meat', 'Butter', 'Cheese', 'Egg']

# Find the middle item(s) of the tuple
length = len(food_stuff_tp)
if length % 2 == 0:
    middle_items = food_stuff_tp[length//2 - 1:length//2 + 1]
else:
    middle_items = food_stuff_tp[length//2]
print("Middle item(s) in the tuple:", middle_items)

# Find the middle item(s) of the list
length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length//2 - 1:length//2 + 1]
else:
    middle_items = food_stuff_lt[length//2]