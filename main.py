#!/usr/bin/python
#standard imports

#other imports

#local imports
import cardboard
from cardboard.deckbox import FrenchFull
from cardboard import board
from cardboard import deck

#general variables
testdeck = deck.Deck([1,1,1,1,1,1,2,2,2,2,2,2,2],['red','brown'])

#rules- move these to rulebook later
fish_board = board.Board(testdeck)
pl_you = fish_board.seat_player('you')
pl_cpu = fish_board.seat_player('cpu')

for player in [pl_you,pl_cpu]:
    player.draw_hand()
    hand = player.hand.held_cards
    print(hand)
    cards_str = [card.__repr__() for card in hand]
    for card in cards_str:
        if cards_str.count(card) > 1:
            print('match')
            continue
        

#functions

#here we go
def main():
    pass

if __name__ == '__main__':
    main()