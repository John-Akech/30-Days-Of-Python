# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

new_companies = {'Spotify', 'Tesla', 'Netflix'}
it_companies.update(new_companies)
print(it_companies)

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

st = set(age)
print(age)
print(st)

if len(age) > len(st):
    print(f"The length of age is bigger")
elif len(age) < len(st):
    print(f"The length of set is bigger") 
else:
    print(f"The lengths of age and set are eaual")
    
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
words = [word.strip('.').lower() for word in words]
unique_words = set(words)
unique_word_count = len(unique_words)
print(f"Unique words: {unique_words}")
print(f"Number of unique words: {unique_word_count}")