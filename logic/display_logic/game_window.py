import pygame
import time
from classes.card.card import Card
from classes.card.deck import Deck
from classes.warrior import Warrior
from classes.board.board import Board
from classes.board.coordinate import Coordinate
from classes.monster import Monster
from logic.game_logic.constants import COLOR, SCREEN, BOARD, CARD

class Game_Window:
    def __init__(self):
        pygame.init()
        SCREEN.initialize()
        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True
        
        # Render board
        board = Board()
        board.render()
        my_deck = Deck(Deck.load_all_cards()[0:5], "bottom")

        # Render monsters
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Update the screen
            SCREEN.screen.fill(COLOR.BACKGROUND)
            board.render()

            # Render the deck
            my_deck.render()

            pygame.display.flip()
        pygame.quit()

