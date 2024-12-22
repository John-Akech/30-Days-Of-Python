import requests
from bs4 import BeautifulSoup
import json

# Step 1: Define the URL to scrape
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Step 2: Fetch the website content
response = requests.get(url)
status = response.status_code
print(status)  # Check if the request was successful (200)

if status == 200:
    print("Successfully fetched the webpage.")

    # Step 3: Parse the content using BeautifulSoup
    content = response.content  # Get the raw HTML content
    soup = BeautifulSoup(content, 'html.parser')  # Parse it with BeautifulSoup
    
    # Step 4: Extract the relevant data
    # For this assignment, extract data in <section> tags
    sections = soup.find_all('section')
    extracted_data = {}  # Store the scraped data here

    for section in sections:
        # Use the first header in the section (if present) as a key
        header = section.find('h2') or section.find('h3') or section.find('h1')
        if header:
            title = header.get_text(strip=True)
            content = section.get_text(strip=True)  # Get all text in the section
            extracted_data[title] = content

    # Step 5: Save the extracted data into a JSON file
    output_file = 'bu_facts_stats.json'
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(extracted_data, file, ensure_ascii=False, indent=4)

    print(f"Data successfully saved to {output_file}")
else:
    print(f"Failed to fetch the webpage. Status code: {status}")