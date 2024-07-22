import genanki

from datetime import date

def save_deck_to(path: str, deck: genanki.Deck):
    today = date.today()
    final_file = f"{path}\\anki_question_{today}.apkg"
    # Writing the deck to a file
    genanki.Package(deck).write_to_file(final_file)
    
def format_examples(examples: list):
    return '<br>'.join([f"- {example}" for example in examples])