from . import deckbox,zones,deck,automaton
from .hand import Hand
from .zones import MissingZone, Zone
from .card import Card

#automatons do the doing
class CardPlayer(automaton.Automaton):
    '''A player of card games. Has some capabliites; more when sat by a Board
    optionall passed a string to name it'''
    def __init__(self, name: str|None = None):
        job = "Card Player"
        super().__init__(job = job, name = name)
        self.hand = Hand(name)
        self.draw_pile: deck.Deck|None = None
        self.discard_zone: Zone|None = None
        self.zones: dict[str, Zone] = {}

    def draw(self, num_cards: int = 1,draw_zone: Zone|None = None):
        '''draw the specified number of cards from the specified zone
        optionally passed a number of cards to draw and a zone to draw from
        will draw one card from the player's draw zone otherwise'''
        if draw_zone:
            #prioritize drawing from specified zone
            self.hand.add(draw_zone.grab_card())
        elif self.draw_pile:
            #second priority to assigned draw zone
            self.hand.add(self.draw_pile.draw())
        else:
            #remember how to throw exceptions or something
            raise zones.MissingZone(f"draw zone is not assigned to {self.name}")
        
    def play(self, 
             play_zone: Zone | None = None,
             play_card: Card | tuple[int,str]|None = None):
        #set play_zone if unset
        if not play_zone and self.zones['play']:
            play_zone = self.zones['play']
        #check again for play zone and fail this time
        if play_zone is None:
            raise MissingZone("no play zone")
        #play random card if play_card unset
        elif not play_card:
            play_zone.put_card(self.hand.play_rand())
        #play specified card
        elif type(play_card) is Card|tuple:
            play_zone.put_card(self.hand.play(play_card))
        
#    def play(self, play_zone: Zone|None = None, to_play: int|list[int]|None = None):
#        '''play the numbered card to the indicated zone
#        optionally passed a Zone and int or list of ints to play from hand
#        will play one card at random to the play zone'''
#        if not play_zone and 'play' in self.zones.keys():
#            play_zone = self.zones['play']
#        if not play_zone:
#            raise zones.MissingZone(f"{self.name} has no zone to play to")
#        if isinstance(to_play,int):    #plays a single card
#            play_zone.put_card(self.hand.play(to_play-1))
#        elif isinstance(to_play,list):  #plays a list of cards
#            for c in to_play:
#                play_zone.put_card(self.hand.play(c-1))
#        elif to_play is not None:   #I'm still learning to use exceptions
#            raise TypeError("cannot play a non-card")
#        else:   #plays a random card if unspecified
#            play_zone.put_card(self.hand.play_rand())

    def discard(self,to_disc: int|list[int]|None = None):
        '''play but for the discard zone'''
        if self.discard_zone:
            self.play(play_zone = self.discard_zone, play_card = to_disc)
        else:
            raise zones.MissingZone(f'discard zone not assigned to {self.name}')
        
    def draw_hand(self,new_hand:bool = False):
        '''will draw up to the player's max hand size
        if new_hand is true, the old hand is discarded'''
        if new_hand and self.hand.card_count() > 0:
            self.discard(list(range(1,self.hand.card_count()+1)))
        while self.hand.card_count() < self.hand.card_max:
            self.draw()


#boards are responsible for keeping track of the rules and the gamestate
#and updating players, zones, etc accordingly
class Board:
    '''holds players, decks, zones, and anything else you need for a game of cards
    pass a deck to start with a draw pile
    start_with_zones = True to generate play and discard zones
    '''
    def __init__(self, start_with_deck: None|deck.Deck = None,
                 start_with_zones: bool = False):
        self.players:dict = {'anon_index': 0}
        self.zones:dict = {'anon_index': 0}
        self.rulebook = None
        if start_with_deck:
            self.zones['draw'] = start_with_deck
        if start_with_zones:
            self.make_zone('discard')
            self.make_zone('play')

    def update_zones(self,player:CardPlayer):
        '''automatically assign draw and discard zones to a player'''
        if "draw" in self.zones.keys():
            player.draw_pile = self.zones['draw']
        if "discard" in self.zones.keys():
            player.discard_zone = self.zones['discard']
        player.zones = self.zones

    def seat_player(self,name: str|None = None):
        '''seat and set up player with optional name'''
        #seat player according to rulebook logic, if present
        if self.rulebook:
            pass
        if not name:
            name = f"Someone{self.players['anon_index']}"
            self.players['anon_index'] += 1
        self.players[name] = CardPlayer(name)
        player = self.players[name]
        #auto adding draw and discard if present in self.zones
        self.update_zones(player)
        return player

    def make_zone(self,name: str|None = None):
        '''create a board zone. pass string to name it'''
        #same deal, eventual rulebook zone
        if self.rulebook:
            pass
        if not name:
            name = f"Some Place{self.players['anon_index']}"
            self.players['anon_index'] += 1
        self.zones[name] = Zone(name)
            

#demos and main down here
def card_player_demo():
    discard_zone = Zone('discard')
    draw_pile = deckbox.FrenchStripped()
    player = CardPlayer('lyra')
    player.draw_pile = draw_pile
    player.discard_zone = discard_zone
    player.draw_hand()
    print(f"{player.hand}\n{player.hand.check_cards()}")
    player.discard()
    print(f"after discarding:\n{player.hand.check_cards()}")

def board_demo():
    demo_board = Board(deckbox.FrenchStripped(),start_with_zones=True)
    demo_board.seat_player('lyra')
    demo_player = demo_board.players['lyra']
    demo_player.draw_hand()
    print("after drawing a hand of 7")
    print(demo_player.hand.check_cards())
    demo_player.play(to_play=[1,2])
    demo_player.discard(to_disc=1)
    print("after playing the first two cards and discarding the third")
    print(demo_player.hand.check_cards())
    print(demo_board.zones['play'])
    print(demo_board.zones['play'].check_cards())

if __name__ == "__main__":
    board_demo()