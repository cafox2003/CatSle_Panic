import pygame
from logic.display_logic.end_screen import End_Screen
from logic.display_logic.menu_screen import Menu_Screen
from logic.game_logic.constants import GAME_WINDOW, SCREEN, initialize
from logic.game_logic.global_state import Global_State 
from logic.display_logic.button import Button


class GUI_CONSTANTS:
    _MENU_BUTTON_DEF_WIDTH = 150
    _MENU_BUTTON_DEF_HEIGHT = 50

    @staticmethod
    def initialize():
        GAME_SCREEN.initialize()
        MENU_SCREEN.initialize()

class MENU_SCREEN:
    _WON = None
    _LOST = None
    _MAIN_MENU = None

    @staticmethod
    def initialize():
        END_BUTTONS = [ 
                       Button(SCREEN.LENGTH // 2 - SCREEN.LENGTH // 10, SCREEN.HEIGHT * 3//4, 
                          GUI_CONSTANTS._MENU_BUTTON_DEF_WIDTH, GUI_CONSTANTS._MENU_BUTTON_DEF_HEIGHT,
                              "Restart game", lambda: MENU_SCREEN.restart_function(), centered=True),

                       Button(SCREEN.LENGTH // 2 + SCREEN.LENGTH // 10, SCREEN.HEIGHT * 3//4, 
                          GUI_CONSTANTS._MENU_BUTTON_DEF_WIDTH, GUI_CONSTANTS._MENU_BUTTON_DEF_HEIGHT,
                              "Main menu", lambda: MENU_SCREEN.main_menu(), centered=True),
                       ]

        MENU_SCREEN._WON = End_Screen(game_won = True, buttons= END_BUTTONS)
        MENU_SCREEN._LOST = End_Screen(game_won = False, buttons= END_BUTTONS)

        MENU_BUTTONS = [
                        Button(SCREEN.LENGTH // 2 - SCREEN.LENGTH // 10, SCREEN.HEIGHT * 3//4,
                          GUI_CONSTANTS._MENU_BUTTON_DEF_WIDTH, GUI_CONSTANTS._MENU_BUTTON_DEF_HEIGHT,
                        "Play game", lambda: MENU_SCREEN.restart_function(), centered=True),

                        Button(SCREEN.LENGTH // 2 + SCREEN.LENGTH // 10, SCREEN.HEIGHT * 3//4, 
                          GUI_CONSTANTS._MENU_BUTTON_DEF_WIDTH, GUI_CONSTANTS._MENU_BUTTON_DEF_HEIGHT,
                        "Exit", lambda: MENU_SCREEN.exit(), centered=True),
                        ]
        MENU_SCREEN._MAIN_MENU = Menu_Screen("Welcome to Castle Panic", MENU_BUTTONS  )
        print("Menu screen initialized")

    @staticmethod
    def restart_function():
        GAME_WINDOW.menu_screen = None

        Global_State.game_state.reset()

    @staticmethod
    def main_menu():
        GAME_WINDOW.menu_screen = MENU_SCREEN._MAIN_MENU

        Global_State.game_state.reset()

    @staticmethod
    def exit():
        pygame.quit()  # Deinitialize pygame
        import sys
        sys.exit()  # Exit the program

    @staticmethod
    def get_end_screen():
        if Global_State.game_state.game_won:
            return MENU_SCREEN._WON
        else:
            return MENU_SCREEN._LOST

class GAME_SCREEN:
    _BUTTONS = None
    @staticmethod
    def initialize():
        mod_horizontal_value = 100
        # GAME_SCREEN._BUTTONS = [
        #     Button(1500 - mod_horizontal_value, 200, 150, 50, "Move", Global_State.game_state.move_monster), # Move button
        #     Button(1700 - mod_horizontal_value, 200, 150, 50, "Add", Global_State.game_state.add_monster), # Add button
        #     Button(1300 - mod_horizontal_value, 200, 150, 50, "Draw cards", Global_State.game_state.draw_cards), # Add button
        #     Button(1100 - mod_horizontal_value, 200, 150, 50, "Next turn", Global_State.game_state.next_turn) # Add button
        #         ]

        GAME_SCREEN._BUTTONS = [
            Button(SCREEN.LENGTH * 0.75 , SCREEN.HEIGHT * 0.25,
                   GUI_CONSTANTS._MENU_BUTTON_DEF_WIDTH, GUI_CONSTANTS._MENU_BUTTON_DEF_HEIGHT,
                   "Next turn", Global_State.game_state.next_turn)
                ]
        print("Successfully initialized!!")

# class SCREEN_HANDLER:
#     @staticmethod
#     def start_new_game():
#         _handler = Screen_Handler()
#         _handler.start_new_game()


# SCREEN_HANDLER = Screen_Handler()
