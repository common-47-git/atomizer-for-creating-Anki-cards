import genanki

from dicts_parse import read_word_definition
from crud import create_anki_deck, create_anki_note, format_examples, save_deck_to

notes: list[genanki.Note] = list()

while True:
    current_word = input("Enter a word or 'exit': ")
    
    if current_word == "exit":
        break 

    # Getting the word definiton from some source
    word = read_word_definition(word=current_word)
    
    if not word["definition"]:
        print(f"Word '{current_word}' not found, make sure you wrote it right.")
        continue 
    
    examples = format_examples(examples=word['examples']) 
    
    card = create_anki_note(word=current_word, definition=word['definition'], examples=examples)
    notes.append(card)

# Specify the name for the deck
deck = create_anki_deck("Knowledge", notes)

# Saving the deck to specified path
path_to_save = r"C:\Users\commo\OneDrive\Рабочий стол"
save_deck_to(path=path_to_save, deck=deck)