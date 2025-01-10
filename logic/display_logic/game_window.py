import pygame
import time
from logic.game_logic.constants import SCREEN, MONSTER
from logic.game_logic.game_state import Game_State

class Game_Window:
    def __init__(self):
        pygame.init()
        SCREEN.initialize()
        MONSTER.initialize()
        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True
        game_state = Game_State()

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_card = my_deck.check_card_click(mouse_pos)
                    if clicked_card:
                        print(f"Clicked on card: {clicked_card.name}")

            game_state.add_monster()
            game_state.move_monsters()
            
            game_state.update_screen()
            time.sleep(1)

            pygame.display.flip()
        pygame.quit()

