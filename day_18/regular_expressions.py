import re  # Importing the `re` module for regular expressions
from collections import Counter  # Importing `Counter` for counting elements

# Paragraph to analyze
paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities to develop 
an application what else can you love.'''

# Clean the paragraph by removing punctuation and converting to lowercase
cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph.lower())

# Find all words in the cleaned paragraph
words = re.findall(r'\w+', cleaned_paragraph)

# Count the occurrences of each word
word_counts = Counter(words)

# Find the most frequent word and its count
most_frequent_word = word_counts.most_common(1)[0] 

# Print the most frequent word and its frequency
print("Most frequent word:", most_frequent_word[0])
print("Frequency:", most_frequent_word[1])

# Text containing numerical positions
text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction."""

# Extract numbers (including negatives) from the text
numbers = re.findall(r'-?\d+', text) 

# Convert the extracted strings to integers
points = list(map(int, numbers))

# Sort the points in ascending order
sorted_points = sorted(points)

# Calculate the distance between the furthest points
distance = sorted_points[-1] - sorted_points[0]

# Print the extracted points, sorted points, and the calculated distance
print("Extracted Points:", points)
print("Sorted Points:", sorted_points)
print("Distance between furthest particles:", distance)

# Function to check if a variable name is valid in Python
def is_valid_variable(variable_name):
    # Regular expression pattern for a valid Python variable name
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    # Return True if the variable name matches the pattern, otherwise False
    return bool(re.match(pattern, variable_name))

# Test the is_valid_variable function with various examples
print(is_valid_variable('first_name'))  # True: Valid variable name
print(is_valid_variable('first-name'))  # False: Contains a hyphen
print(is_valid_variable('1first_name')) # False: Starts with a number
print(is_valid_variable('firstname'))   # True: Valid variable name

# Function to clean a given text
def clean_text(sentence):
    # Remove special characters from the text
    cleaned = re.sub(r'[^\w\s]', '', sentence) 
    # Replace multiple spaces with a single space
    cleaned = re.sub(r'\s+', ' ', cleaned) 
    # Strip leading and trailing spaces
    return cleaned.strip()

# Function to find the three most frequent words in cleaned text
def most_frequent_words(cleaned_text):
    # Split the cleaned text into words
    words = cleaned_text.split()
    # Count occurrences of each word
    word_counts = Counter(words)
    # Get the three most common words with their counts
    most_common = word_counts.most_common(3)
    return most_common

# Sentence with special characters to clean
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting 
&and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u 
to be a tea@cher!?'''

# Clean the sentence
cleaned_text = clean_text(sentence)
print("Cleaned Text:", cleaned_text)

# Find the three most frequent words in the cleaned text
most_frequent = most_frequent_words(cleaned_text)
print("Most Frequent Words:", most_frequent)