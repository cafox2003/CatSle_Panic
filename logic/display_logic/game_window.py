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

        my_hero = Warrior("knight" ,"blue")

        my_card = my_hero.card
        # card_2 = Card(">:D", "An EVIL guy...", image_path="images/face.png")
        # card_3 = Card("D:", "He's worried", image_path="images/face.png")
        # card_4 = Card(":3", "A little face", image_path="images/face.png")
        # card_5 = Card(":3", "A little face", image_path="images/face.png")
        # card_6 = Card(":3", "A little face", image_path="images/face.png")
        # all_cards = [my_card, card_2, card_3, card_4, card_5]

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

