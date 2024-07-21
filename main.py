import genanki

from datetime import date
import random

from dicts_parse import get_word_definition
from anki_models import my_model
from crud import save_deck_to

notes: list[genanki.Note] = list()

while True:
    current_word = input("Enter a word or 'exit': ")
    
    if current_word == "exit":
        break 

    # Getting the word definiton from some source
    current_word_definition = get_word_definition(word=current_word)
    
    if not current_word_definition:
        print(f"Word '{current_word}' not found, make sure you wrote it right.")
        continue 
    
    # Creating the Anki note
    current_note = genanki.Note(
        model=my_model,
        fields=[f"{current_word}", f"{current_word_definition}"]
    )

    notes.append(current_note)

# Generating a random deck ID
deck_id = random.randrange(1 << 30, 1 << 31)

# Print the generated deck ID
print("model id -", deck_id)

# Creating the Anki deck and adding the notes to it
my_deck = genanki.Deck(deck_id, "Knowledge")
for note in notes:
    my_deck.add_note(note)
    
# Saving the deck to specified path
save_deck_to(path=r"C:\Users\commo\OneDrive\Рабочий стол\-\genanki")