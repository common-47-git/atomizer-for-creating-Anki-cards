import genanki 

from pydantic_models.word_card import WordCardDTO

from dictionaries import cambridge_dict
from src.automizer_base import AnkiAutomizerBase
from src.automizers.en_to_en import crud


class EnToEnCLI(AnkiAutomizerBase):
    
    def run(self) -> None:

        notes: list[genanki.Note] = list()
        
        while True:
            
            word = WordCardDTO()
            word.spelling = input("Enter a word or 'exit': ")
            
            if word.spelling == "exit":
                break 

            # Getting the word definiton from some source
            word = cambridge_dict.read_word_definition(word=word)
            
            
            card = crud.create_anki_note(word=word.spelling, 
                                           definition=word.definition, 
                                           examples=word.format_examples())
            notes.append(card)
             
        deck = crud.create_anki_deck(self.deck_name, notes)
                
        crud.save_deck(path=self.path_to_save, deck=deck)
        
        