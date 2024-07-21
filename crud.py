import genanki

from datetime import date

from main import my_deck

def save_deck_to(path: str):
    today = date.today()
    final_file = f"{save_to}\\anki_question_{today}.apkg"
    # Writing the deck to a file
    genanki.Package(my_deck).write_to_file(final_file)
