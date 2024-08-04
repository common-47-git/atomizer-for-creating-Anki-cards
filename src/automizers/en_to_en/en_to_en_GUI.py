import genanki 
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)
from PySide6.QtWidgets import (
    QApplication,
)

from dictionaries import cambridge_dict
from pydantic_models.word_card import WordCardDTO
from src.automizers.en_to_en import crud
from src.automizers.en_to_en.ui_mainWindow import Ui_MainWindow


class EnToEnGUI(QtWidgets.QMainWindow):
    
    notes: list[genanki.Note] = list()
    
    def __init__(self, path_to_save, deck_name="AutoDeck"):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_add_to_deck_clicked)
        self.ui.lineEdit.returnPressed.connect(self.on_add_to_deck_clicked)

        self.deck_name = deck_name
        self.path_to_save = path_to_save
        
    def on_add_to_deck_clicked(self):
        word = WordCardDTO()
        word.spelling = self.ui.lineEdit.text()
        
        if not word.spelling:
            return
        
        self.ui.lineEdit.clear()
        
        # Getting the word definiton from some source
        word = cambridge_dict.read_word_definition(word=word)
        
        if not word.definition:
            self.ui.textBrowser.append(f"Word '{word.spelling}' not found.")
            return
        
        card = crud.create_anki_note(word=word.spelling, 
                                       definition=word.definition, 
                                       examples=word.format_examples())
        self.notes.append(card)
             
        deck = crud.create_anki_deck(self.deck_name, self.notes)
                
        crud.save_deck(path=self.path_to_save, deck=deck)
        
        self.ui.textBrowser.append(word.spelling)


app = QApplication([])
