import pygame
from logic.game_logic.constants import GAME_WINDOW, SCREEN, COLOR, GAME_STATE, initialize
from logic.game_logic.global_state import Global_State 
# Global_State.game_state.game_won
from logic.display_logic.button import Button
from logic.display_logic.end_screen import End_Screen

from logic.display_logic.gui_constants import END_SCREEN

class Game_Window:
    def __init__(self):
        self.initialize()

    def initialize(self):

        initialize()
        Global_State.initialize()
        END_SCREEN.initialize()

        self.run = True
        self.end_screen = None
        GAME_WINDOW.menu_screen = None
        
        # TODO: Make another class and maybe store button definitions in constants
        self.buttons = [
            Button(1500, 200, 150, 50, "Move", Global_State.game_state.move_monster), # Move button
            Button(1700, 200, 150, 50, "Add", Global_State.game_state.add_monster), # Add button
            Button(1300, 200, 150, 50, "Draw cards", Global_State.game_state.draw_cards), # Add button
            Button(1100, 200, 150, 50, "Next turn", Global_State.game_state.next_turn) # Add button
                ]

        self.main_loop()

    def main_loop(self): #Maybe change name

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # print(f"{GAME_WINDOW.menu_screen}")
                    self.check_click() 

            self.update_game()

        pygame.quit()

        
    def update_game(self):
        Global_State.game_state.check_game_status()


        if Global_State.game_state.game_over:
            if GAME_WINDOW.menu_screen == None:
                GAME_WINDOW.menu_screen = END_SCREEN.get_end_screen()
                GAME_WINDOW.menu_screen.display()
            # self.run = self.end_screen()
        else:
            self.update_screen()

        # self.run = not Global_State.game_state.game_over

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

        # self.check_click()
        pygame.display.flip()

    # Handle all clicks
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        self.check_buttons(mouse_pos)
        self.check_cards(mouse_pos)
        self.check_monsters(mouse_pos)


        if GAME_WINDOW.menu_screen != None:
            GAME_WINDOW.menu_screen.check_buttons()

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
