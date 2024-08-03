from src.automizers.en_to_en import EnToEnCLI, EnToEnGUI

# python3 -m pip install -r .\requirements.txt
# python3 main.py

if __name__ == "__main__":
    #app = EnToEnCLI(path_to_save=r"C:\Users\commo\OneDrive\Рабочий стол")
    automizer = EnToEnGUI()
    automizer.deck_name = "My English Deck"
    automizer.path_to_save = "./"
    automizer.run()