from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QMessageBox, QFileDialog, QVBoxLayout, QLabel,
    QGroupBox, QCheckBox, QWidget, QScrollArea, QDialog
)

import genanki
from dictionaries import cambridge_dict
from pydantic_models.word_card import WordCardDTO
from src.automizers.en_to_en import crud
from src.automizers.en_to_en.ui_mainWindow import Ui_MainWindow


class DefinitionWindow(QDialog):

    checked_words: list[WordCardDTO] = list()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Definitions")
        self.setMinimumSize(600, 250)

        # Create a scroll area for definitions
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Container for the content inside the scroll area
        self.scroll_area_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)

        # Layout for the dialog
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)

    def add_definition_groupbox(self, word: WordCardDTO, checked_definitions: int, current_definition: int):
        group_box = QGroupBox(word.spelling)
        group_box.setCheckable(True)
        
        # Only check the first "checked_definitions" number of definitions
        if current_definition <= checked_definitions:
            group_box.setChecked(True)
        else:
            group_box.setChecked(False)  # Uncheck the others by default
        
        group_box_layout = QVBoxLayout(group_box)

        definition_label = QLabel(word.definition)
        definition_label.setWordWrap(True)
        bold_font = QFont()
        bold_font.setBold(True)
        definition_label.setFont(bold_font)
        group_box_layout.addWidget(definition_label)

        italic_font = QFont()
        italic_font.setItalic(True)

        for example in word.examples:
            checkbox = QCheckBox(example)
            checkbox.setFont(italic_font)
            checkbox.setChecked(True)  # Set all examples to be checked by default
            group_box_layout.addWidget(checkbox)

        self.scroll_layout.addWidget(group_box)

        return group_box  # Return the group box for later checking

    def clear_definitions(self):
        """Clears all dynamically added group boxes from the layout."""
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def closeEvent(self, event):
        """Override closeEvent to clear definitions before closing and store checked words."""
        self.save_checked_words()  # Store checked words before closing
        self.clear_definitions()  # Clear definitions when window is closed
        for word in self.checked_words:
            print(word)
        for word in self.checked_words:
            card = crud.create_anki_note(word=word.spelling, 
                                        definition=word.definition, 
                                        examples=word.format_examples())
            EnToEnGUI.notes.append(card)
        event.accept()  # Accept the close event so the window closes

    def save_checked_words(self):
        """Append checked words and examples to the checked_words list."""
        self.checked_words.clear()  # Clear previous checked words if any

        # Iterate through each group box in the scroll layout
        for i in range(self.scroll_layout.count()):
            group_box = self.scroll_layout.itemAt(i).widget()

            if isinstance(group_box, QGroupBox) and group_box.isChecked():
                word = WordCardDTO(
                    spelling=group_box.title(),
                    definition=group_box.findChild(QLabel).text(),
                    examples=[checkbox.text() for checkbox in group_box.findChildren(QCheckBox) if checkbox.isChecked()]
                )
                self.checked_words.append(word)  # Add to the list of checked words


class EnToEnGUI(QMainWindow):
    notes: list[genanki.Note] = list()
    checked_definitions: int = 1  # Limit of checked definitions by default

    def __init__(self, path_to_save=None, deck_name="AutoDeck"):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set layout for central widget if not set
        if not self.ui.centralwidget.layout():
            self.central_layout = QVBoxLayout(self.ui.centralwidget)
            self.ui.centralwidget.setLayout(self.central_layout)
        else:
            self.central_layout = self.ui.centralwidget.layout()

        # Connect actions to methods
        self.ui.extract_button.clicked.connect(self.extract_clicked)
        self.ui.save_deck_button.clicked.connect(self.on_save_deck_clicked)
        self.ui.save_to_button.clicked.connect(self.save_to_button_clicked)
        self.ui.lineEdit.returnPressed.connect(self.extract_clicked)

        # Instance variables
        self.deck_name = deck_name
        self.path_to_save = path_to_save
        self.previous_word: str
        self.spelling: str

        # Definition Window instance (initially hidden)
        self.definition_window = DefinitionWindow()

    def extract_clicked(self):
        self.spelling = self.ui.lineEdit.text().strip()

        if not self.spelling:
            return

        self.previous_word = self.spelling
        self.ui.lineEdit.clear()

        words: list[WordCardDTO] = cambridge_dict.read_word_definition(word_spelling=self.spelling)

        if not words:
            self.ui.textBrowser.append(f"Word '{self.spelling}' not found.")
            return

        # Show definition window and add definitions
        self.definition_window.show()
        for current_word, word in enumerate(words, 1):
            self.definition_window.add_definition_groupbox(
                word=word, 
                checked_definitions=self.checked_definitions, 
                current_definition=current_word)

        self.ui.textBrowser.append(f"{self.spelling}")

    def save_to_button_clicked(self):
        options = QFileDialog.Options()
        self.path_to_save = QFileDialog.getExistingDirectory(self, "Open directory", "", options=options)

    def on_save_deck_clicked(self):
        if not self.path_to_save:
            QMessageBox.information(self, "Error", "Please choose a directory to save your deck.")
            return

        deck = crud.create_anki_deck(self.deck_name, self.notes)
        crud.save_deck(path=self.path_to_save, deck=deck)
        QMessageBox.information(self, "Success", "Anki deck saved successfully!")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up and self.previous_word:
            self.ui.lineEdit.setText(self.previous_word)
            event.accept()
        else:
            super().keyPressEvent(event)


app = QApplication([])


