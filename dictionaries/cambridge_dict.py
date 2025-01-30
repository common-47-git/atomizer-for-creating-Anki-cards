import requests
from bs4 import BeautifulSoup as BS
from pydantic_models.word_card import WordCardDTO

def read_word_definition(word_spelling: str) -> list[WordCardDTO]:
    url = f"https://dictionary.cambridge.org/dictionary/english/{word_spelling}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"No access to the dict: {e}")
        return []

    soup = BS(response.text, 'lxml')

    # Find all definitions
    definition_blocks = soup.find_all('div', class_='ddef_h')

    if not definition_blocks:
        print(f"Word '{word_spelling}' not found, make sure you wrote it right.")
        return []

    words = []

    for definition_block in definition_blocks:
        # Extract definition text
        definition_div = definition_block.find('div', class_='def ddef_d db')
        if not definition_div:
            continue

        definition_text = ' '.join(definition_div.get_text(separator=' ').split()).replace(':', '').strip()

        # Create a WordCardDTO object
        word_dto = WordCardDTO(spelling=word_spelling, definition=definition_text)

        # Find corresponding examples (inside the next 'def-body' div)
        examples = []
        def_body = definition_block.find_next_sibling('div', class_='def-body ddef_b')
        
        if def_body:
            example_divs = def_body.find_all('div', class_='examp dexamp', limit=word_dto.examples_to_extract)
            for div in example_divs:
                example_text = ' '.join(div.get_text(separator=' ').split()).strip()
                if example_text:
                    examples.append(example_text)

        word_dto.examples = examples
        words.append(word_dto)

    return words

