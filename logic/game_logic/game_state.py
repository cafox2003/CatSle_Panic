from classes.monster import Monster
from classes.player import Player
from classes.card.deck import Deck
from classes.board.board import Board
from logic.game_logic.constants import SCREEN, COLOR

class Game_State:
    def __init__(self, players = 1):# Add everything
        self.monster_deck = Monster.generate_monsters()
        self.active_monsters = []

        self.card_deck = Deck.load_all_cards() # ADD this
        self.discard_pile = [] # ADD this

        self.players = [Player(deck = self.card_deck, discard = self.discard_pile)]
        
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


    def add_monster(self):
        self.active_monsters.append(self.monster_deck.pop())

    def move_monsters(self):
        for monster in self.active_monsters:
            if monster.health == 0:
                active_monsters.remove(monster)
            else:
                monster.move()

    # TODO: Move to game window
    def update_screen(self):
        # Board
        SCREEN.screen.fill(COLOR.BACKGROUND)
        self.board.render()

        #Decks
        for p in self.players:
            p.deck.render()

        #Monsters
        for monster in self.active_monsters:
            monster.render()

    

