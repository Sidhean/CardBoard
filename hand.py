from card import Card
from random import randint
class Hand:
    def __init__(self, holder: str|None = None, card_max: int=7, card_min: int=0, starting_cards: int=0):
        self.held_cards: list[Card]=[]
        self.holder=holder if holder else 'Someone'
        self.card_max=card_max
        self.card_min=card_min
        self._cared_count=None
        if starting_cards:
            pass #draw starting_cards Cards once I have draw defined

    def __str__(self):
        return f"Hand of {self.holder}: {self.card_count()}/{self.card_max}"
    def __repr__(self):
        return f"Hand({self.holder}, {self.card_max}, {self.card_min = })"

    def card_count(self):
        return len(self.held_cards)
    def check_cards(self):
        num_card_names: str = ''
        card_number = 1
        for card in self.held_cards:
            num_card_names += f"{card_number}: {card}\n"
            card_number += 1
        return num_card_names
    
    def add(self, card):
        self.held_cards.append(card)
    def play(self, card_index: int=0):
        return self.held_cards.pop(card_index)
    def play_rand(self):
        max_index = self.card_count()
        if max_index < 1:
            raise ValueError("No cards to play randomly")
        return self.held_cards.pop(randint(0,(max_index-1)))

if __name__ == "__main__":
    my_hand = Hand('lyra')
    my_hand.add(Card(4,'green'))
    my_hand.add(Card(12,'red'))
    print(my_hand)
    print(my_hand.check_cards())
    my_hand.play(1)
    print("after playing card 1")
    print(my_hand)
    print(my_hand.check_cards())
