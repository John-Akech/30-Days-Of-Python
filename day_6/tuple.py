empty_tpl = tuple()
print(empty_tpl)

names_of_siblings = ('Kuot', 'Abuk', 'Adhieu', 'Awel')
print(names_of_siblings)

brothers_tuple = ('Deng', 'Kuot')
print(brothers_tuple)
sisters_tuple = ('Abuk', 'Adhieu', 'Awel')
print(sisters_tuple)

siblings_tpl = brothers_tuple + sisters_tuple
print(siblings_tpl)

parents = ('Father', 'Mother')
family_members = siblings_tpl + parents
print(family_members)

siblings = family_members[:5]
print(f"siblings: {siblings}")

parent = family_members[5:]
print(f"parents: {parent}")

fruits = ('Apple', 'Banana', 'Cherry', 'Mango')
print(fruits)

vegetables = ('Cabbage', 'Egg plant', 'Irish potatoes')
print(vegetables)

animal_products = ('Milk', 'Meat', 'Butter', 'Cheese', 'Egg')
print(animal_products)

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# For tuple 
length = len(food_stuff_tp)
if length % 2 == 0:
    middle_items = food_stuff_tp[length//2 - 1:length//2 + 1]
else:
    middle_items = food_stuff_tp[length//2]

print("Middle item(s) in the tuple:", middle_items)

# For list
length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length//2 - 1:length//2 + 1]
else:
    middle_items = food_stuff_lt[length//2]