import genanki 
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)
from PySide6.QtCore import (
    QCoreApplication, 
    QMetaObject,
    QRect
)
from PySide6.QtWidgets import (
    QApplication, 
    QGridLayout, 
    QLineEdit,   
    QPushButton, 
    QTextBrowser,
    QWidget,
)
from pydantic_models.word_card import WordCardDTO


from dictionaries import cambridge_dict
from src.automizers.en_to_en import crud


class EnToEnGUI(QtWidgets.QMainWindow):
    
    notes: list[genanki.Note] = list()
    
    def __init__(self, path_to_save, deck_name="AutoDeck"):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow()
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
        


class UI_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(330, 200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 310, 180))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add to deck", None))
    # retranslateUi


app = QApplication([])
