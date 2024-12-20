import os

def count_lines_and_words(file_path):
    """
    Counts the number of lines and words in a given text file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        tuple: A tuple containing the number of lines and the number of words.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)  # Number of lines
            word_count = sum(len(line.split()) for line in lines)  # Count words in each line
            return line_count, word_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0, 0

# Folder containing the text files
data_folder = "data"

# List of file names
files = [
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt"
]

# Process each file
for file_name in files:
    file_path = os.path.join(data_folder, file_name)
    lines, words = count_lines_and_words(file_path)
    print(f"{file_name}:\n  Lines: {lines}\n  Words: {words}\n")

import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    """
    Finds the top N most spoken languages from a JSON file.

    Args:
        filename (str): Path to the JSON file containing countries data.
        top_n (int): Number of top languages to return.

    Returns:
        list: A list of tuples where each tuple contains the count and the language.
    """
    try:
        # Load data from the JSON file
        with open(filename, 'r', encoding='utf-8') as file:
            countries = json.load(file)

        # Extract all languages from the data
        languages = []
        for country in countries:
            languages.extend(country.get('languages', []))

        # Count occurrences of each language
        language_counts = Counter(languages)

        # Get the top N most spoken languages
        most_common = language_counts.most_common(top_n)
        return most_common

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON file: {filename}")
        return []

# Test the function with the example inputs
print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))
print(most_spoken_languages(filename='./data/countries_data.json', top_n=3))


import json

def most_populated_countries(filename, top_n):
    """
    Finds the top N most populated countries from a JSON file.

    Args:
        filename (str): Path to the JSON file containing countries data.
        top_n (int): Number of top countries to return.

    Returns:
        list: A list of dictionaries with country names and populations.
    """
    try:
        # Load data from the JSON file
        with open(filename, 'r', encoding='utf-8') as file:
            countries = json.load(file)

        # Extract country names and populations into a list of dictionaries
        country_population = [
            {'country': country['name'], 'population': country['population']}
            for country in countries
        ]

        # Sort countries by population in descending order
        sorted_countries = sorted(country_population, key=lambda x: x['population'], reverse=True)

        # Return the top N countries
        return sorted_countries[:top_n]

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON file: {filename}")
        return []

# Test the function with the example inputs
print(most_populated_countries(filename='./data/countries_data.json', top_n=10))
print(most_populated_countries(filename='./data/countries_data.json', top_n=3))


import re

def extract_email_addresses(filename):
    """
    Extracts all email addresses from a text file.

    Args:
        filename (str): Path to the text file.

    Returns:
        list: A list of unique email addresses.
    """
    try:
        # Open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regular expression to find email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

        # Return unique email addresses
        return list(set(emails))

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Extract and print email addresses from the file
email_addresses = extract_email_addresses('email_exchange_big.txt')
print(email_addresses)


from collections import Counter
import re

def find_most_common_words(source, num_words):
    """
    Finds the most common words in a string or file.

    Args:
        source (str): Text content or path to a file.
        num_words (int): Number of top common words to return.

    Returns:
        list: A list of tuples with word frequency in descending order.
    """
    try:
        # Check if source is a file or string
        if source.endswith('.txt'):
            # Read file content
            with open(source, 'r', encoding='utf-8') as file:
                text = file.read()
        else:
            # Use the source directly as text
            text = source

        # Clean the text and split into words
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation, lowercase
        words = cleaned_text.split()  # Split text into words

        # Count word frequencies
        word_counts = Counter(words)

        # Get the most common words
        most_common = word_counts.most_common(num_words)

        return most_common

    except FileNotFoundError:
        print(f"File not found: {source}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
print(find_most_common_words('sample.txt', 10))
print(find_most_common_words('sample.txt', 5))


# Function to find the most frequent words in a text file
from collections import Counter
import re

def find_most_common_words(source, num_words):
    """
    Finds the most common words in a string or file.

    Args:
        source (str): Text content or path to a file.
        num_words (int): Number of top common words to return.

    Returns:
        list: A list of tuples with word frequency in descending order.
    """
    try:
        # Check if source is a file or string
        if source.endswith('.txt'):
            # Read file content
            with open(source, 'r', encoding='utf-8') as file:
                text = file.read()
        else:
            # Use the source directly as text
            text = source

        # Clean the text and split into words
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation, lowercase
        words = cleaned_text.split()  # Split text into words

        # Count word frequencies
        word_counts = Counter(words)

        # Get the most common words
        most_common = word_counts.most_common(num_words)

        return most_common

    except FileNotFoundError:
        print(f"File not found: {source}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Find the ten most frequent words in Obama's speech
obama_speech = './data/obama_speech.txt'
print("Obama's 10 Most Frequent Words:")
print(find_most_common_words(obama_speech, 10))

# Find the ten most frequent words in Michelle Obama's speech
michelle_speech = './data/michelle_obama_speech.txt'
print("\nMichelle Obama's 10 Most Frequent Words:")
print(find_most_common_words(michelle_speech, 10))

# Find the ten most frequent words in Trump's speech
trump_speech = './data/donald_speech.txt'
print("\nTrump's 10 Most Frequent Words:")
print(find_most_common_words(trump_speech, 10))

# Find the ten most frequent words in Melania Trump's speech
melania_speech = './data/melina_trump_speech.txt'
print("\nMelania Trump's 10 Most Frequent Words:")
print(find_most_common_words(melania_speech, 10))