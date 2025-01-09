import pygame
import time
from classes.card.card import Card
from classes.card.deck import Deck
from classes.board.board import Board
from classes.board.coordinate import Coordinate
from classes.monster import Monster
from logic.game_logic.constants import COLOR, SCREEN, BOARD, CARD, MONSTER

class Game_Window:
    def __init__(self):
        pygame.init()
        SCREEN.initialize()
        # MONSTER.initialize()
        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True
        
        # Render board
        board = Board()
        board.render()
        my_deck = Deck(Deck.load_all_cards()[0:5], "bottom")

        # all_monsters = Monster.generate_monsters()
        all_monsters = []
        for i in range(36):
            all_monsters.append(Monster.create_monster(monster_type = "troll", number = ((i % 6) + 1)))

        current_monsters = []

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_card = my_deck.check_card_click(mouse_pos)
                    if clicked_card:
                        print(f"Clicked on card: {clicked_card.name}")

            # Update the screen
            SCREEN.screen.fill(COLOR.BACKGROUND)
            board.render()

            # Render the deck
            my_deck.render()

            current_monsters.append(all_monsters.pop())
            # current_monsters.append(all_monsters.pop())
            for monster in current_monsters:
                if monster.health == 0:
                    current_monsters.remove(monster)
                else:
                    monster.render()
                    monster.move()
                    monster.damage()
            time.sleep(1)

            pygame.display.flip()
        pygame.quit()

