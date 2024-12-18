from random import randint
from .card import Card


class Hand:
    def __init__(
        self,
        holder: str | None = None,
        card_max: int = 7,
        card_min: int = 0,
        starting_cards: int = 0,
    ):
        self.held_cards: list[Card] = []
        self.holder = holder if holder else "Someone"
        self.card_max = card_max
        self.card_min = card_min
        self._cared_count = None
        if starting_cards:
            pass  # draw starting_cards Cards once I have draw defined

    def __str__(self):
        return f"Hand of {self.holder}: {self.card_count()}/{self.card_max}"

    def __repr__(self):
        return f"Hand({self.holder}, {self.card_max}, {self.card_min = })"

    def __iter__(self):
        return iter(self.held_cards)

    # methods that check things
    def card_count(self, key: Card | tuple[int, str] | None = None):
        if key is None:
            return len(self.held_cards)
        else:
            rank, suit = Card.parse_card(key)
            card_count = 0
            for card in self:
                if card.rank == rank and card.suit == suit:
                    card_count += 1
            return card_count

    def check_cards(self):
        num_card_names: str = ""
        card_number = 1
        for card in self.held_cards:
            num_card_names += f"{card_number}: {card}\n"
            card_number += 1
        return num_card_names

    def has_a_match(self, count: int = 2):
        hand_str = [card.__repr__() for card in self]
        for card in hand_str:
            if hand_str.count(card) >= count:
                return True

    # methods that do things
    def add(self, card):
        self.held_cards.append(card)

    def play(self, card_to_play: Card | tuple[int, str] | int):
        if type(card_to_play) is Card:
            return self.held_cards.pop(self.held_cards.index(card_to_play))
        elif type(card_to_play) is tuple:
            rank, suit = card_to_play
            for card in self:   #loop to search for card match
                if card.rank == rank and card.suit == suit:
                    card_index = self.held_cards.index(card)
                    return self.held_cards.pop(card_index)  #return stops 'for'
        elif type(card_to_play) is int:
            return self.held_cards.pop(card_to_play)

    def play_rand(self):
        max_index = self.card_count()
        if max_index < 1:
            raise ValueError("No cards to play randomly")
        return self.held_cards.pop(randint(0, (max_index - 1)))

    def play_set(
        self,
        pair_key: Card | tuple[int | None, str | None] | None = None,
        set_count: int = 2,
    ):
        if pair_key:
            rank, suit = Card.parse_card(pair_key)
        else:
            rank, suit = None, None
        pairs = set()  # i can't get this to work with cards themselves
        res = []
        for card in self:
            # skips card if var is set AND it doesn't match the key
            if rank and card.rank != rank:
                continue
            elif suit and card.suit.lower() != suit.lower():
                continue
            elif (
                self.card_count(card) >= set_count
                and (card.rank, card.suit) not in pairs
            ):
                pairs.add((card.rank, card.suit))
        for _ in range(set_count):
            for pair in pairs:
                res.append(self.play(pair))
        return res


if __name__ == "__main__":
    my_hand = Hand("lyra")
    my_hand.add(Card(4, "green"))
    my_hand.add(Card(12, "red"))
    print(my_hand)
    print(my_hand.check_cards())
    my_hand.play(1)
    print("after playing card 1")
    print(my_hand)
    print(my_hand.check_cards())
