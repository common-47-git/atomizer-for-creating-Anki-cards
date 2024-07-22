import genanki
from pydantic import BaseModel

from datetime import date

from schemas.word import WordBase
from anki_models.word_card import anki_word_card
from dictionaries import cambridge_dict

class AnkiAutomizer(BaseModel):
    
    deck_name: str = "English2"
    path_to_save: str = None
    
    def run(self) -> None:
        notes: list[genanki.Note] = list()

        while True:
            
            word = WordBase()
            word.spelling = input("Enter a word or 'exit': ")
            
            if word.spelling == "exit":
                break 

            # Getting the word definiton from some source
            word = cambridge_dict.read_word_definition(word=word)
            
            if not word.definition:
                print(f"Word '{word.spelling}' not found, make sure you wrote it right.")
                continue
            
            word.examples = word.format_examples() 
            
            card = self.__create_anki_note(word=word.spelling, definition=word.definition, examples=word.examples)
            notes.append(card)
             
        deck = self.__create_anki_deck(self.deck_name, notes)
                
        self.__save_deck(path=self.path_to_save, deck=deck)
    
    
    def __create_anki_note(self, word: str, definition: str, examples: str):
        card = genanki.Note(
            model=anki_word_card,
            fields=[word, definition, examples]
        )
        return card


    def __create_anki_deck(self, name: str, notes: list[genanki.Note]):
        deck = genanki.Deck(1234567890, name)
        for note in notes:
            deck.add_note(note)
        return deck
    

    def __save_deck(self, path: str, deck: genanki.Deck):
        today = date.today()
        final_file = f"{path}\\anki_question_{today}.apkg"
        genanki.Package(deck).write_to_file(final_file)

  