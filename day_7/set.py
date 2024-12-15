# Define sets and a list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Print the length of the set 'it_companies'
print(len(it_companies))  # Output: 7

# Add 'Twitter' to the 'it_companies' set
it_companies.add('Twitter')
print(it_companies)  # Now includes 'Twitter'

# Create a new set of companies and update 'it_companies' with them
new_companies = {'Spotify', 'Tesla', 'Netflix'}
it_companies.update(new_companies)
print(it_companies)  # Now includes 'Spotify', 'Tesla', and 'Netflix'

# Set operations on A and B
print(A.union(B))  # Union: All unique elements from both sets
print(A.intersection(B))  # Intersection: Common elements in both sets
print(A.issubset(B))  # Check if A is a subset of B (True or False)
print(A.isdisjoint(B))  # Check if A and B have no common elements (True or False)
print(A.symmetric_difference(B))  # Elements that are in either A or B, but not in both

# Convert 'age' list to a set to remove duplicates
st = set(age)
print(age)  # Original list with duplicates
print(st)  # Set (unique values)

# Compare the lengths of the list and set
if len(age) > len(st):
    print(f"The length of age is bigger")
elif len(age) < len(st):
    print(f"The length of set is bigger") 
else:
    print(f"The lengths of age and set are equal")

# Working with words in a sentence
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()  # Split sentence into words
words = [word.strip('.').lower() for word in words]  # Remove punctuation and convert to lowercase
unique_words = set(words)  # Create a set of unique words
unique_word_count = len(unique_words)  # Count unique words
print(f"Unique words: {unique_words}")  # Print the set of unique words
print(f"Number of unique words: {unique_word_count}")  # Print the count of unique words