# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(330, 200)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(12, 12))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 311, 181))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.add_to_deck_button = QPushButton(self.widget)
        self.add_to_deck_button.setObjectName(u"add_to_deck_button")

        self.gridLayout.addWidget(self.add_to_deck_button, 0, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 2)

        self.save_deck_button = QPushButton(self.widget)
        self.save_deck_button.setObjectName(u"save_deck_button")

        self.gridLayout.addWidget(self.save_deck_button, 2, 0, 1, 1)

        self.choose_folder_button = QPushButton(self.widget)
        self.choose_folder_button.setObjectName(u"choose_folder_button")

        self.gridLayout.addWidget(self.choose_folder_button, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AnkiAutomizer", None))
        self.add_to_deck_button.setText(QCoreApplication.translate("MainWindow", u"Add to deck", None))
        self.save_deck_button.setText(QCoreApplication.translate("MainWindow", u"Save deck", None))
        self.choose_folder_button.setText(QCoreApplication.translate("MainWindow", u"Choose folder", None))
    # retranslateUi

