from classes.monster.monster_deck import Monster_Deck
from classes.player import Player
from classes.card.deck import Deck
from classes.board.board import Board
from logic.game_logic.constants import GAME_STATE

class Game_State:
    def __init__(self, players = 1):# Add everything
        self.monster_deck = Monster_Deck()

        # TODO: Create a class that handles the discard_pile as well
        self.card_deck = Deck.load_all_cards() 
        self.discard_pile = [] 

        self.players = [Player(full_deck = self.card_deck, discard = self.discard_pile)]
        
        self.board = Board()

        self.game_over = False
        self.game_won = None

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
        player.load_hand(self.card_deck, self.discard_pile, GAME_STATE.NUM_CARDS)

    def remove_card(self, player = None):
        if player == None:
            player = self.players[0]
        player.remove_card(self.discard_pile)

    def next_turn(self):
        self.monster_deck.move_monsters(self.board)
        
        for _ in range(GAME_STATE.NUM_DRAW_MONSTERS):
            self.monster_deck.add_monster()

        self.draw_cards()

    def check_game_status(self):
        # Checks if any towers exist
        towers_exist = any(not tower.destroyed for tower in self.board.castles["towers"])

        monsters_remain = self.monster_deck.monsters_remain()
        

        if not towers_exist:
            self.game_over = True
            self.game_won = False
        elif not monsters_remain:
            self.game_over = True
            self.game_won = True
            print(f" Game over: {self.game_over}\nGame won: {self.game_won}")
        



    # Wrapper functions to be called from game window for testing
    def add_monster(self):
        self.monster_deck.add_monster()

    def move_monster(self):
        self.monster_deck.move_monsters(self.board)
