import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def __str__(self) -> str:
        # string
        return 'This is a FrenchDeck object from str'
    
    def __repr__(self) -> str:
        # fallback
        # representation
        return 'This is a FrenchDeck object from repr'
    
print(FrenchDeck())
print(str(FrenchDeck()))

deck = FrenchDeck()
print(deck)