import genanki 
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QMessageBox,
    QFileDialog,
)

from dictionaries import cambridge_dict
from pydantic_models.word_card import WordCardDTO
from src.automizers.en_to_en import crud
from src.automizers.en_to_en.ui_mainWindow import Ui_MainWindow


from PyQt6.QtCore import Qt

class EnToEnGUI(QtWidgets.QMainWindow):
    
    notes: list[genanki.Note] = list()
    
    def __init__(self, path_to_save=None, deck_name="AutoDeck"):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_to_deck_button.clicked.connect(self.on_add_to_deck_clicked)
        self.ui.save_deck_button.clicked.connect(self.on_save_deck_clicked)
        self.ui.choose_folder_button.clicked.connect(self.on_choose_folder_button_clicked)
        self.ui.lineEdit.returnPressed.connect(self.on_add_to_deck_clicked)

        self.deck_name = deck_name
        self.path_to_save = path_to_save
        self.previous_word: str
        self.spelling: str
        
    def on_add_to_deck_clicked(self):
        self.spelling = self.ui.lineEdit.text()
        
        if not self.spelling:
            return

        self.previous_word = self.spelling
        self.ui.lineEdit.clear()
        
        # Fetch definitions
        words = cambridge_dict.read_word_definition(word_spelling=self.spelling)
        
        if not words:
            self.ui.textBrowser.append(f"Word '{self.spelling}' not found.")
            return

        for word in words:
            card = crud.create_anki_note(word=word.spelling, 
                                        definition=word.definition, 
                                        examples=word.format_examples())
            self.notes.append(card)

            self.ui.textBrowser.append(f"{word.spelling}: {word.definition}")
    
    
    def on_choose_folder_button_clicked(self):
        options = QFileDialog.Options()
        self.path_to_save = QFileDialog.getExistingDirectory(self, "Open directory", "", options=options)
    

    def on_save_deck_clicked(self):
        if not self.path_to_save:
            QMessageBox.information(self, "You did not choose any directory!", "Please choose a directory to save your deck.")
            return
        
        deck = crud.create_anki_deck(self.deck_name, self.notes)
        crud.save_deck(path=self.path_to_save, deck=deck)
        QMessageBox.information(self, "Success", "Anki deck saved successfully!")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Up:
            if self.previous_word:
                self.ui.lineEdit.setText(self.previous_word)
        else:
            super().keyPressEvent(event)

app = QApplication([])
