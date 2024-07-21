from bs4 import BeautifulSoup as BS
import requests

def get_word_definition(word):
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
    div_content = soup.find('div', class_='def ddef_d db')

    if div_content:
        definition = div_content.get_text(separator=' ')
        cleaned_definition = ' '.join(definition.split()).replace(':', '').strip()
        return cleaned_definition
    else:
        return None

word = "hold"   
print("'", get_word_definition(word), "'")