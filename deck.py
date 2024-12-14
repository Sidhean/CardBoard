from card import Card
from random import shuffle


class Deck: # count should modify the number of times the deck is repeated,
            # or the number of total cards if random is True
            #index 0 is, conceptually, the bottom of the deck
            #append to add to top. pop to take top card.
    """no fix more permanant than a temporary docstring"""

    def __init__(
        self,
        ranks: list[int],
        suits: list[(str)],
        extra_cards=[],
        label: str | None = None,
        random: bool = False,
        count=1,
        shuf=True,
    ):
        self.ranks = ranks
        self.suits = suits
        self.label = label if label else 'Some Deck'
        self.is_random = random
        self.count = count
        self.extra_cards = extra_cards
        self.cards: list[Card] = []
        self.return_pile: list[Card] = []
        self.stack_deck()
        if shuf:
            self.shuffle_up()
    def __str__(self):
        return self.label.capitalize()

    def stack_deck(self):
        self.cards = []
        for s in self.suits:
            for r in self.ranks:
                self.cards.append(Card(r, s))
        if self.extra_cards:
            for card in self.extra_cards:
                self.cards.append(card)
            
    def draw(self) -> Card:
        return self.cards.pop(0)

    def add_to(self, card: Card):
        self.cards.append(card)

    def shuffle_up(self, new_deck=False):
        if new_deck:
            self.stack_deck()
            self.return_pile = []
        self.cards += self.return_pile
        shuffle(self.cards)

    def put_back(self, card: Card | list[Card]):
        if isinstance(card, Card):
            self.return_pile.insert(0, card)
        elif isinstance(card, list):
            for c in card:
                self.return_pile.append(c)

    def discard(self, card):
        self.return_pile.append(card)

    def card_count(self):
        return len(self.cards)

if __name__ == "__main__":
    this_deck = Deck(list(range(12)),['A','B','C'])
    print("drawing three cards")
    for _ in range(3):
        print(this_deck.draw())