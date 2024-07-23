from pydantic import BaseModel

class AnkiAutomizer(BaseModel):
    
    deck_name: str = "AutoDeck"
    path_to_save: str
  