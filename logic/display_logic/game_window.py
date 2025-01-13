import pygame
import time
from logic.game_logic.constants import SCREEN, MONSTER, COLOR 
from logic.game_logic.global_state import Global_State 
from logic.display_logic.button import Button

from classes.board.castle.castle import Castle
from logic.game_logic.constants import SCREEN, BOARD

class Game_Window:
    def __init__(self):
        pygame.init()
        SCREEN.initialize()
        MONSTER.initialize()
        Global_State.initialize()
        
        # TODO: Make another class and maybe store button definitions in constants
        self.buttons = [
            # Button(1500, 200, 150, 50, "Move", Global_State.game_state.monster_deck.move_monsters), # Move button
            # Button(1700, 200, 150, 50, "Add", Global_State.game_state.monster_deck.add_monster), # Add button
            # Button(1300, 200, 150, 50, "Draw cards", Global_State.game_state.draw_cards), # Add button
            Button(1100, 200, 150, 50, "Next turn", Global_State.game_state.next_turn) # Add button
                ]

        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True

        for _ in range(6):
            Global_State.game_state.monster_deck.add_monster()

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
        Global_State.game_state.board.render()

        #Decks
        for p in Global_State.game_state.players:
            p.deck.render()

        #Monsters
        for monster in Global_State.game_state.monster_deck.active_monsters:
            monster.render()

        # Buttons
        for button in self.buttons:
            button.render()

        # my_castle = Castle(2, BOARD.HEXAGON_DISTANCE)
        # my_castle.render()

        pygame.display.flip()

    # Handle all clicks
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        self.check_buttons(mouse_pos)
        self.check_cards(mouse_pos)
        self.check_monsters(mouse_pos)

    # Handle button clicks
    def check_buttons(self, mouse_pos):
        for button in self.buttons:
            button.check_click(mouse_pos)

    # Handle card clicks
    def check_cards(self, mouse_pos):
        for player in Global_State.game_state.players:
            clicked_card = player.deck.check_card_click(mouse_pos)

            if clicked_card:
                if clicked_card.card_type == "Warrior":
                    # Highlight all monster cards 
                    Global_State.game_state.monster_deck.highlight_monsters(clicked_card) 

                self.update_screen()

    #Handle monster clicks
    def check_monsters(self, mouse_pos):
        for monster in Global_State.game_state.monster_deck.active_monsters:
            if monster.check_click(mouse_pos) and monster.is_highlighted:
                # Global_State.game_state.players[0].deck.remove_card()
                Global_State.game_state.remove_card()

                Global_State.game_state.monster_deck.unhighlight_monsters()

                is_defeated = monster.damage()  # Damage the monster
                if is_defeated:
                    Global_State.game_state.monster_deck.defeat_monster(monster)
                self.update_screen()
                break  # Stop after the first monster is clicked
