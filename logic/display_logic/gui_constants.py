from logic.display_logic.end_screen import End_Screen
from logic.game_logic.constants import GAME_WINDOW, SCREEN, GAME_STATE
from logic.game_logic.global_state import Global_State 
from logic.display_logic.button import Button

def initialize():
    END_SCREEN.initialize()

class END_SCREEN:
    _WON = None
    _LOST = None

    @staticmethod
    def initialize():
        BUTTONS = [ Button(SCREEN.LENGTH // 2, SCREEN.HEIGHT * 3//4, 150, 50, "Restart game", lambda: END_SCREEN.restart_function(), centered=True) ]
        END_SCREEN._WON = End_Screen(game_won = True, buttons= BUTTONS)
        END_SCREEN._LOST = End_Screen(game_won = False, buttons= BUTTONS)

    @staticmethod
    def restart_function():
        GAME_WINDOW.menu_screen = None

        Global_State.game_state.reset()

    @staticmethod
    def get_end_screen():
        if Global_State.game_state.game_won:
            return END_SCREEN._WON
        else:
            return END_SCREEN._LOST


# class SCREEN_HANDLER:
#     @staticmethod
#     def start_new_game():
#         _handler = Screen_Handler()
#         _handler.start_new_game()


# SCREEN_HANDLER = Screen_Handler()
