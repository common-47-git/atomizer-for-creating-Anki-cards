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
        MainWindow.resize(353, 232)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(12, 12))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 331, 211))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.extract_button = QPushButton(self.layoutWidget)
        self.extract_button.setObjectName(u"extract_button")

        self.gridLayout.addWidget(self.extract_button, 0, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 2)

        self.save_deck_button = QPushButton(self.layoutWidget)
        self.save_deck_button.setObjectName(u"save_deck_button")

        self.gridLayout.addWidget(self.save_deck_button, 2, 0, 1, 1)

        self.save_to_button = QPushButton(self.layoutWidget)
        self.save_to_button.setObjectName(u"save_to_button")

        self.gridLayout.addWidget(self.save_to_button, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AnkiAutomizer", None))
        self.extract_button.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.save_deck_button.setText(QCoreApplication.translate("MainWindow", u"Save deck", None))
        self.save_to_button.setText(QCoreApplication.translate("MainWindow", u"Save to", None))
    # retranslateUi

