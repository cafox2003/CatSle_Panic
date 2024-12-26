import pygame
import time
from classes.card import Card
from classes.board.board import Board
from classes.board.coordinate import Coordinate
from classes.monster import Monster
from logic.game_logic.constants import SCREEN, BOARD

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

        # Render monsters
        # monsters = [Monster.create_from_template("orc", i) for i in range(1,7)]
        all_monsters = Monster.generate_monsters()
        current_monsters = []

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Update the screen
            SCREEN.screen.fill((0,0,0))
            board.render()

            current_monsters.append(all_monsters.pop())

            for monster in current_monsters:
                monster.render()
                monster.move()
            time.sleep(1)

            if len(all_monsters) == 0:
                run = False

            pygame.display.flip()
        pygame.quit()

