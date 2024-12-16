"""
Explain the difference between map, filter, and reduce.

map: Applies a function to each element of a list and returns a new list with the transformed elements.
Example: [1, 2, 3].map(x => x * 2) => [2, 4, 6]

filter: Filters elements in a list based on a condition and returns a new list with only the elements that meet the condition.
Example: [1, 2, 3, 4].filter(x => x % 2 === 0) => [2, 4]

reduce: Reduces a list to a single value by applying a function repeatedly to an accumulator and each element.
Example: [1, 2, 3].reduce((acc, x) => acc + x, 0) => 6
"""

"""
Explain the difference between higher-order functions, closures, and decorators.
Higher-order function: A function that takes another function as an argument or returns a function.
Example: map, filter, reduce.

Closure: A function that captures variables from its surrounding scope and remembers them even when the scope is gone.
"""
## Example:

def outer():
    x = 10
    def inner():
        return x
    return inner
f = outer()
print(f())  

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
for country in countries:
    print(country)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


countries_upper = map(lambda country: country.upper(), countries)
print(list(countries_upper))

squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))

names_upper = map(lambda name: name.upper(), names)
print(list(names_upper))

countries_with_land = filter(lambda country: 'land' in country, countries)
print(list(countries_with_land))

countries_with_six_chars = filter(lambda country: len(country) == 6, countries)
print(list(countries_with_six_chars))

countries_with_six_or_more = filter(lambda country: len(country) >= 6, countries)
print(list(countries_with_six_or_more))

countries_starting_with_E = filter(lambda country: country.startswith('E'), countries)
print(list(countries_starting_with_E))

result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(list(result))

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

print(get_string_lists([1, "Hello", 3.14, "World"]))

from functools import reduce
total_sum = reduce(lambda acc, x: acc + x, numbers)
print(total_sum)

sentence = reduce(lambda acc, country: acc + ", " + country, countries)
sentence += " are north European countries"
print(sentence)

def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country, countries))

print(categorize_countries("land"))

from collections import defaultdict

def country_letter_count(countries):
    letter_count = defaultdict(int)
    for country in countries:
        letter_count[country[0]] += 1
    return dict(letter_count)

print(country_letter_count(countries))

def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(countries))

def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(countries))
