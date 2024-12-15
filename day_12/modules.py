import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id

print(random_user_id())

def user_id_gen_by_user():
    
    num_char = int(input('Enter the number of characters for each ID: '))
    num_ids = int(input('Enter the number of IDs to generate: '))
   
    characters = string.ascii_letters + string.digits
    ids = []
    for i in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_char))
        ids.append(user_id)
    
    return '\n'.join(ids)

print(user_id_gen_by_user())

def rgb_color_gen():
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())

def list_of_hexa_colors(num_colors):
    
    hex_colors = []
    
    for _ in range(num_colors):
        
        hex_color = f"#{''.join(random.choices('0123456789abcdef', k=6))}"
        
        hex_colors.append(hex_color)
    
    return hex_colors

print(list_of_hexa_colors(5)) 

def  list_of_rgb_colors(num_colors):
    
    rgb_colors = []
    
    for i in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        rgb_colors.append((r, g, b))
    return rgb_colors
print(list_of_rgb_colors(6))

def generate_colors(color_type, num_colors):
    colors = []
    
    if color_type == 'hexa':
        for _ in range(num_colors):
            hex_color = f"#{''.join(random.choices('0123456789abcdef', k=6))}"
            colors.append(hex_color)
    
    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb_color = f"rgb({r}, {g}, {b})"
            colors.append(rgb_color)
    
    return colors

print(generate_colors('hexa', 3)) 
print(generate_colors('hexa', 1)) 
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print(shuffled_list)

def unique_random_numbers():
    
    return random.sample(range(10), 7)

random_numbers = unique_random_numbers()
print(random_numbers)