import collections

# 1. collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

card = Card('7', 'diamonds')
print(card)

# 2. from scratch
class Card:
    def __init__(self, rank, suit):
        self.rank: str = rank
        self.suit: str = suit

    def __repr__(self):
        # representation of the object
        return f'Card(rank={self.rank!r}, suit={self.suit!r})'

card = Card(7, 'diamonds')
print(card)

# 3. from typing
from typing import NamedTuple

class Card(NamedTuple):
    rank: str
    suit: str

card = Card(7, 'diamonds')
print(card)

# 4. dataclass
from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str

card = Card(7, 'diamonds')
print(card)

# 5. pydantic
from pydantic import BaseModel

class Card(BaseModel):
    rank: str
    suit: int

card = Card(rank=7, suit='diamonds')
print(card)
