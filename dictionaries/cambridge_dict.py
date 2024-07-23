import requests
from bs4 import BeautifulSoup as BS

from DTOs.word import WordDTO

def read_word_definition(word: WordDTO) -> WordDTO:
    url = f"https://dictionary.cambridge.org/dictionary/english/{word.spelling}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"No access to the dict: {e}")
        return word

    soup = BS(response.text, 'lxml')

    # Extract definition
    definition_div = soup.find('div', class_='def ddef_d db')
    if definition_div:
        word.definition = ' '.join(definition_div.get_text(separator=' ').split()).replace(':', '').strip()

    # Extract examples
    example_divs = soup.find_all('div', class_='examp dexamp')
    for word.examples_to_extract, div in enumerate(example_divs):
        if word.examples_to_extract > 3:
            break
        example_text = ' '.join(div.get_text(separator=' ').split()).strip()
        if example_text:
            word.examples.append(example_text)
        
    return word
