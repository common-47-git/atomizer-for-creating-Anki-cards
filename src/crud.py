import genanki

from datetime import date

from models.word_card_model import word_card_model

def create_anki_note(word: str, definition: str, examples: str):
    card = genanki.Note(
        model=word_card_model,
        fields=[word, definition, examples]
    )
    return card

def create_anki_deck(name: str, notes: list[genanki.Note]):
    deck = genanki.Deck(1234567890, name)
    for notes in notes:
        deck.add_note(notes)
    return deck

def save_deck_to(path: str, deck: genanki.Deck):
    today = date.today()
    final_file = f"{path}\\anki_question_{today}.apkg"
    # Writing the deck to a file
    genanki.Package(deck).write_to_file(final_file)
    
def format_examples(examples: list):
    return '<br>'.join([f"- {example}" for example in examples])