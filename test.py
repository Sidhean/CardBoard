#!/usr/bin/python
from random import shuffle
from cardboard import hand, deck, card

card_parser = card.Card.parse_card
my_hand = hand.Hand("me")
this_deck = deck.Deck([1,1,2,2], ['swoen'],count=5)
shuffle(this_deck.cards)

def draw_til_pair(hand: hand.Hand):
    while not hand.has_a_match():
        hand.add(this_deck.draw())
for _ in range(5):
    my_hand.add(this_deck.draw())
draw_til_pair(my_hand)

print(my_hand.check_cards())
while my_hand.has_a_match(3):
    this_deck.put_back(my_hand.play_set(set_count = 3))
print(f"{my_hand.check_cards() = }\n{this_deck.return_pile = }")
