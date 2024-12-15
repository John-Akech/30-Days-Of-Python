import random
import string

# Function to generate a random user ID with 6 alphanumeric characters
def random_user_id():
    # Create a pool of characters (letters and digits)
    characters = string.ascii_letters + string.digits
    # Randomly select 6 characters to form a user ID
    user_id = ''.join(random.choices(characters, k=6))
    return user_id

# Print a random user ID
print(random_user_id())

# Function to generate multiple user IDs based on user input
def user_id_gen_by_user():
    # Ask the user for the number of characters in each ID
    num_char = int(input('Enter the number of characters for each ID: '))
    # Ask the user for the number of IDs to generate
    num_ids = int(input('Enter the number of IDs to generate: '))
   
    # Pool of characters for the user ID
    characters = string.ascii_letters + string.digits
    ids = []
    
    # Generate the requested number of user IDs
    for i in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_char))
        ids.append(user_id)
    
    # Return the generated IDs, each on a new line
    return '\n'.join(ids)

# Print the generated user IDs
print(user_id_gen_by_user())

# Function to generate a random RGB color
def rgb_color_gen():
    # Generate random values for red, green, and blue components
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Return the RGB color in string format
    return f"rgb({r}, {g}, {b})"

# Print a random RGB color
print(rgb_color_gen())

# Function to generate a list of random hexadecimal colors
def list_of_hexa_colors(num_colors):
    hex_colors = []
    
    # Generate the specified number of hexadecimal colors
    for _ in range(num_colors):
        # Generate a random hexadecimal color code
        hex_color = f"#{''.join(random.choices('0123456789abcdef', k=6))}"
        hex_colors.append(hex_color)
    
    # Return the list of hexadecimal colors
    return hex_colors

# Print a list of 5 random hexadecimal colors
print(list_of_hexa_colors(5))

# Function to generate a list of random RGB colors
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    
    # Generate the specified number of RGB colors
    for i in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        # Append the RGB color as a tuple (r, g, b) to the list
        rgb_colors.append((r, g, b))
    
    # Return the list of RGB colors
    return rgb_colors

# Print a list of 6 random RGB colors
print(list_of_rgb_colors(6))

# Function to generate either hexadecimal or RGB colors based on user input
def generate_colors(color_type, num_colors):
    colors = []
    
    # Check if the user wants hexadecimal colors
    if color_type == 'hexa':
        for _ in range(num_colors):
            hex_color = f"#{''.join(random.choices('0123456789abcdef', k=6))}"
            colors.append(hex_color)
    
    # Check if the user wants RGB colors
    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb_color = f"rgb({r}, {g}, {b})"
            colors.append(rgb_color)
    
    # Return the generated colors
    return colors

# Print random hexadecimal and RGB colors
print(generate_colors('hexa', 3))  # List of 3 hexadecimal colors
print(generate_colors('hexa', 1))  # List of 1 hexadecimal color
print(generate_colors('rgb', 3))   # List of 3 RGB colors
print(generate_colors('rgb', 1))   # List of 1 RGB color

# Function to shuffle a list randomly
def shuffle_list(lst):
    # Shuffle the list in place
    random.shuffle(lst)
    return lst

# Example list to shuffle
my_list = [1, 2, 3, 4, 5]
# Shuffle the list and print the result
shuffled_list = shuffle_list(my_list)
print(shuffled_list)

# Function to generate a list of unique random numbers
def unique_random_numbers():
    # Generate a list of 7 unique random numbers in the range [0, 9]
    return random.sample(range(10), 7)

# Print a list of unique random numbers
random_numbers = unique_random_numbers()
print(random_numbers)
