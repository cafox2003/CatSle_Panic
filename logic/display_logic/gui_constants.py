import pygame
from logic.display_logic.end_screen import End_Screen
from logic.display_logic.menu_screen import Menu_Screen
from logic.game_logic.constants import GAME_WINDOW, SCREEN
from logic.game_logic.global_state import Global_State 
from logic.display_logic.button import Button

def initialize():
    MENU_SCREEN.initialize()

class MENU_SCREEN:
    _WON = None
    _LOST = None
    _MAIN_MENU = None

    @staticmethod
    def initialize():
        END_BUTTONS = [ 
                       Button(SCREEN.LENGTH // 2, SCREEN.HEIGHT * 3//4, 
                          150, 50, "Restart game", lambda: MENU_SCREEN.restart_function(), centered=True),
                       Button(SCREEN.LENGTH // 2 + 200, SCREEN.HEIGHT * 3//4, 
                          150, 50, "Main menu", lambda: MENU_SCREEN.main_menu(), centered=True),
                       ]

        MENU_SCREEN._WON = End_Screen(game_won = True, buttons= END_BUTTONS)
        MENU_SCREEN._LOST = End_Screen(game_won = False, buttons= END_BUTTONS)

        MENU_BUTTONS = [
                        Button(SCREEN.LENGTH // 2, SCREEN.HEIGHT * 3//4, 150, 50,
                        "1 player game", lambda: MENU_SCREEN.restart_function(), centered=True),

                        Button(SCREEN.LENGTH // 2 + 200, SCREEN.HEIGHT * 3//4, 150, 50,
                        "Exit", lambda: MENU_SCREEN.exit(), centered=True),
                        ]
        MENU_SCREEN._MAIN_MENU = Menu_Screen("Welcome to Castle Panic", MENU_BUTTONS  )

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


# class SCREEN_HANDLER:
#     @staticmethod
#     def start_new_game():
#         _handler = Screen_Handler()
#         _handler.start_new_game()


# SCREEN_HANDLER = Screen_Handler()
