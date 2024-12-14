from deck import Deck
from card import Card

class DeckConstr(Deck):
    '''Creates a Deck out of a DeckConstr Class.
       DeckType(
       ranks: list[int|str], 
       suits: list[str] #optional
       label: str, extra_cards: list[Card]  #optional
       )
    '''
    def __init__(self, deck_constr: dict):
        ranks: list = deck_constr['ranks']
        suits: list[str] = deck_constr['suits']
        label: str = deck_constr['label']
        if 'extra_cards' in deck_constr.keys():
            extra_cards: list[Card] = deck_constr['extra_cards']
        else:
            extra_cards: list[Card] = []
        
        super().__init__(ranks, suits, label=label, extra_cards=extra_cards)


class FrenchFull(DeckConstr):
    def __init__(self):
        ff_params = {'ranks': list(range(2, 16)),
                     'suits': ["Spade", "Heart", "Club", "Diamond"],
                     'label': "French Full"}
        super().__init__(ff_params)


class FrenchStripped(DeckConstr):
    def __init__(self):
        fs_params = {
            'ranks': list(range(9, 16)),
            'suits': ["Spade", "Heart", "Club", "Diamond"],
            'label': "French Stripped"
        }
        super().__init__(fs_params)


class Spanish(DeckConstr):
    def __init__(self):
        s_params = {'ranks': list(range(1, 11)), 'suits': ["Cup", "Coin", "Club", "Sword"], 'label': "Spanish"}
        super().__init__(s_params)


class Tarot(DeckConstr):
    def __init__(self):
        major_arcana = (
            "The Fool",
            "The Magician",
            "The High Priestess",
            "The Empress",
            "The Emperor",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgement",
            "The World",
        )
        t_params = {
            'ranks': list(range(1, 15)),
            'suits': ["Wand", "Cup", "Sword", "Pentacle"],
            'label': "Tarot",
            'extra_cards': major_arcana
        }
        super().__init__(t_params)

if __name__ == '__main__':
    demo_deck = FrenchFull()
    print("five cards from the French Full deck")
    for _ in range(5):
        print(demo_deck.draw())