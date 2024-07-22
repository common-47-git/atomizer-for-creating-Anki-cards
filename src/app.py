import genanki

from dictionaries.cambridge_dict import read_word_definition
from models.word_card_model import word_card_model
from src.crud import format_examples, save_deck_to

class AnkiAutomizer:
    
    def __init__(self) -> None:
        pass
    
    def run(self) -> None:
        notes: list[genanki.Note] = list()

        while True:
            current_word = input("Enter a word or 'exit': ")
            
            if current_word == "exit":
                break 

            # Getting the word definiton from some source
            parsed_word = read_word_definition(word=current_word)
            
            if not parsed_word:
                print(f"Word '{current_word}' not found, make sure you wrote it right.")
                continue 
            
            examples = format_examples(examples=parsed_word['examples']) 
            
            card = self.__create_anki_note(word=current_word, definition=parsed_word['definition'], examples=examples)
            notes.append(card)
             
        # Specify the name for the deck
        deck = self.__create_anki_deck("English2", notes)
                
        # Saving the deck to specified path
        path_to_save = r"C:\Users\Andrew\Desktop"
        save_deck_to(path=path_to_save, deck=deck)
    
    def __create_anki_note(self, word: str, definition: str, examples: str):
        card = genanki.Note(
            model=word_card_model,
            fields=[word, definition, examples]
        )
        return card

    def __create_anki_deck(self, name: str, notes: list[genanki.Note]):
        deck = genanki.Deck(1234567890, name)
        for note in notes:
            deck.add_note(note)
        return deck
    
    
    