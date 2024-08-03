from pydantic import BaseModel

class AnkiAutomizerBase(BaseModel):
    
    deck_name: str = "AutoDeck"
    path_to_save: str
  