import genanki

from datetime import date

from anki_note_types.word_card import word_card_model
from DTOs.word_card import WordCardDTO
from dictionaries import cambridge_dict
from src.automizer import AnkiAutomizer

class EnToEnAutomizer(AnkiAutomizer):
    
    def run_CLI(self) -> None:
        notes: list[genanki.Note] = list()

        while True:
            
            word = WordCardDTO()
            word.spelling = input("Enter a word or 'exit': ")
            
            if word.spelling == "exit":
                break 

            # Getting the word definiton from some source
            word = cambridge_dict.read_word_definition(word=word)
            
            card = self.__create_anki_note(word=word.spelling, 
                                           definition=word.definition, 
                                           examples=word.format_examples())
            notes.append(card)
             
        deck = self.__create_anki_deck(self.deck_name, notes)
                
        self.__save_deck(path=self.path_to_save, deck=deck)
    
        
    def run(self) -> None:
        notes: list[genanki.Note] = list()
      
     
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
    
    def __save_deck(self, path: str, deck: genanki.Deck):
        today = date.today()
        final_file = f"{path}\\anki_question_{today}.apkg"
        genanki.Package(deck).write_to_file(final_file)
        