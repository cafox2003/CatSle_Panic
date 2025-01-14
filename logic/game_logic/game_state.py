from classes.monster.monster_deck import Monster_Deck
from classes.player import Player
from classes.card.deck import Deck
from classes.board.board import Board

class Game_State:
    def __init__(self, players = 1):# Add everything
        self.monster_deck = Monster_Deck()

        # TODO: Create a class that handles the discard_pile as well
        self.card_deck = Deck.load_all_cards() 
        self.discard_pile = [] 

        self.players = [Player(full_deck = self.card_deck, discard = self.discard_pile)]
        
        self.board = Board()

        """card_deck,
        players - list of all players
            player - individual player object (have multiple in a list):
                player_hands - implement as a deck obj,
                is_player_turn - true/false for if it's their is_player_turn
                slain_monsters[] - a list of monsters they've slain
            all_turns_over - stores if all players have finished their turn
        monster_deck - all monsters still in the pile
        draw_new_monsters - boolean that keeps track of if more monsters can be drawn (missing hasn't been drawn, monsters still left)
        active_monsters - List of all active monsters,
       """

    def draw_cards(self, player = None):
        if player == None:
            player = self.players[0]
        player.load_hand(self.card_deck, self.discard_pile, 6)

    def remove_card(self, player = None):
        if player == None:
            player = self.players[0]
        player.remove_card(self.discard_pile)

    def next_turn(self):
        self.monster_deck.move_monsters(self.board)
        
        for i in range(2):
            self.monster_deck.add_monster()

        self.draw_cards()
