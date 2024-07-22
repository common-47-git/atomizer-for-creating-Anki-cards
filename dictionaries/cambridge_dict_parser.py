import requests
from bs4 import BeautifulSoup as BS

EXAMPLES_TO_EXTRACT = 3

def read_word_definition(word):
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BS(response.text, 'lxml')

    # Extract definition
    definition_div = soup.find('div', class_='def ddef_d db')
    if definition_div:
        definition = ' '.join(definition_div.get_text(separator=' ').split()).replace(':', '').strip()
    else:
        definition = None

    # Extract examples
    examples = []
    example_divs = soup.find_all('div', class_='examp dexamp')
    for EXAMPLES_TO_EXTRACT, div in enumerate(example_divs):
        if EXAMPLES_TO_EXTRACT > 3:
            break
        example_text = ' '.join(div.get_text(separator=' ').split()).strip()
        if example_text:
            examples.append(example_text)
        
    if not definition:
        return None
    else:
        result = {'definition': definition, 'examples': examples}
        return result
