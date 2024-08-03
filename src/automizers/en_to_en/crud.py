import genanki 

from datetime import date

from anki_note_types.word_card import word_card_model

def create_anki_note(word: str, definition: str, examples: str):
        card = genanki.Note(
            model=word_card_model,
            fields=[word, definition, examples]
        )
        return card


def create_anki_deck(name: str, notes: list[genanki.Note]):
    deck = genanki.Deck(1234567890, name)
    for note in notes:
        deck.add_note(note)
    return deck


def save_deck(path: str, deck: genanki.Deck):
    today = date.today()
    final_file = f"{path}\\anki_question_{today}.apkg"
    genanki.Package(deck).write_to_file(final_file)
