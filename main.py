#from src.automizers.en_to_en.en_to_en_CLI import EnToEnCLI
from src.automizers.en_to_en.en_to_en_GUI import EnToEnGUI, app

# For developing
# pyside6-uic .\src\automizers\en_to_en\ui_mainWindow.ui -o ui_mainWindow.py
# pyside6-rcc .\src\icons\icons_resources.qrc -o icons_resources_rc.py      


# To install
# python -m venv venv
# .\venv\Scripts\activate
# python3 -m pip install -r .\requirements.txt
# python3 main.py

# To run
# .\venv\Scripts\activate
# python3 main.py

if __name__ == "__main__":
    #app = EnToEnCLI(path_to_save=r"C:\Users\commo\OneDrive\Рабочий стол")
    #app.run()

    window = EnToEnGUI(path_to_save=r"C:\Users\Andrew\Desktop")
    window.show()
    app.exec()