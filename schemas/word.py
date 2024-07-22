from pydantic import BaseModel

class WordBase(BaseModel):
    spelling: str | None = None
    definition: str | None = None
    examples: list[str] = []
    examples_to_extract: int = 3
    
    def format_examples(self) -> str:
        return '<br>'.join([f"- {example}" for example in self.examples])
