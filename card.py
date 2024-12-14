class Card:
    """A card for use with Decks and Hands."""

    def __init__(self, rank: int, suit: str, standard=True):
        self.rank = int(rank)
        self.suit = suit
        self.standard = standard
        self.name = f"{self.rank} of {self.suit}s"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Card({self.rank}, {self.suit}, {self.standard})"

if __name__ == "__main__":
    cards = []
    for r in range(5):
        for s in ['blue','green','orange']:
            cards.append(Card(r,s))
    print('some cards:')
    for card in cards:
        print(card)