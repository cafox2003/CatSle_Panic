import pygame
import time
from logic.game_logic.constants import SCREEN, MONSTER, COLOR
from logic.game_logic.game_state import Game_State
from logic.display_logic.button import Button

class Game_Window:
    def __init__(self):
        pygame.init()
        SCREEN.initialize()
        MONSTER.initialize()

        self.game_state = Game_State()

        self.buttons = [
            Button(1500, 200, 150, 50, "Move", self.game_state.move_monsters), # Move button
            Button(1700, 200, 150, 50, "Add", self.game_state.add_monster) # Add button
                ]

        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True

        for _ in range(10):
            self.game_state.add_monster()

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click() 

            self.update_screen()
        pygame.quit()

    # Calls everything's render method to update the screen
    def update_screen(self):
        # Board
        SCREEN.screen.fill(COLOR.BACKGROUND)
        self.game_state.board.render()

        #Decks
        for p in self.game_state.players:
            p.deck.render()

        #Monsters
        for monster in self.game_state.active_monsters:
            monster.render()

        # Buttons
        for button in self.buttons:
            button.render()

        pygame.display.flip()

    # Handle all clicks
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        self.check_buttons(mouse_pos)
        self.check_cards(mouse_pos)

    # Handle button clicks
    def check_buttons(self, mouse_pos):
        for button in self.buttons:
            button.check_click(mouse_pos)

    # Handle card clicks
    def check_cards(self, mouse_pos):
        for player in self.game_state.players:
            clicked_card = player.deck.check_card_click(mouse_pos)
            if clicked_card:
                # print(f"Clicked on card: {clicked_card.ring}")
                if clicked_card.card_type == "Warrior":
                    for monster in self.game_state.active_monsters:
                        # print(f"Monster ring: {monster.coordinate.ring}\tCard ring: {clicked_card.ring}\nMonster color: {monster.coordinate.color}\tCard color: {clicked_card.color}")
                        if (monster.coordinate.ring == clicked_card.ring) and (monster.coordinate.color == clicked_card.color):
                            monster.is_highlighted = True
                        elif (monster.coordinate.ring == clicked_card.ring) and (clicked_card.color == "any_color"):
                            monster.is_highlighted = True
                        elif (clicked_card.ring == "hero" and monster.coordinate.ring != "forest") and (monster.coordinate.color == clicked_card.color):
                            monster.is_highlighted = True
                        else:
                            monster.is_highlighted = False

                self.update_screen()

