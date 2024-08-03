#from src.automizers.en_to_en.en_to_en_CLI import EnToEnCLI
from src.automizers.en_to_en.en_to_en_GUI import EnToEnGUI, app

# python3 -m pip install -r .\requirements.txt
# python3 main.py

if __name__ == "__main__":
    #app = EnToEnCLI(path_to_save=r"C:\Users\commo\OneDrive\Рабочий стол")
    #app.run()

    window = EnToEnGUI(path_to_save=r"C:\Users\commo\OneDrive\Рабочий стол")
    window.show()
    app.exec()