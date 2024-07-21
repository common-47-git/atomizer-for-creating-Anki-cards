import genanki

import random

# Generating a random model ID
model_id = random.randrange(1 << 30, 1 << 31)

# Creating the Anki model
my_model = genanki.Model(
    model_id,
    "Knowledge",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card type 1",
            "qfmt": "<div style='text-align: center; font-size: 24px;'>{{Question}}</div>",
            "afmt": "<div style='text-align: center; font-size: 24px;'>{{FrontSide}} <hr id='answer'> {{Answer}} <hr id='examples'> </div>",
        },
    ]
)