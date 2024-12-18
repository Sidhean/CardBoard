from .card import Card
from cardboard import card
#zone ideas:
#deck storage: keeps deck, active/inactive status, and original owner


class Zone:
    def __init__(self, zone_name: str):
        self.name: str = zone_name
        self.contents: list = []

    def __str__(self):
        if self.name in ('draw','discard','play'):
            name = f"{self.name.capitalize()} Zone"
        else:
            name = self.name
        return name.replace("_", " ")

    def check_cards(self):
        num_zones: str = ''
        zone_number = 1
        for card in self.contents:
            num_zones += f"{zone_number}: {card}\n"
            zone_number += 1
        return num_zones
            

    def grab_card(self, card_to_grab: int|None = None):
        if card_to_grab:
            card_grabbed: Card = self.contents.pop(card_to_grab)
            return card_grabbed
        return self.contents.pop()

    def put_card(self, card_to_put: Card|None):
        if card_to_put:
            self.contents.append(card_to_put)


class MissingZone(Exception):
    '''raise if accessed zone is not assigned'''
    pass

if __name__ == "__main__":
    new_zone = Zone('demo zone')
    print(new_zone)
    new_zone.put_card(Card(1,'black'))
    print(new_zone.check_cards())