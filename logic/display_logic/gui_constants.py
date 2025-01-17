from logic.display_logic.end_screen import End_Screen
from logic.game_logic.constants import SCREEN, initialize 
from logic.game_logic.global_state import Global_State 
from logic.display_logic.button import Button
from logic.display_logic.screen_handler import Screen_Handler

def initialize():
    END_SCREEN.initialize()

class END_SCREEN:
    _WON = None
    _LOST = None

    @staticmethod
    def initialize():
        BUTTONS = [ Button(SCREEN.LENGTH // 2, SCREEN.HEIGHT * 3//4, 150, 50, "Restart game", lambda: SCREEN_HANDLER.start_new_game(), centered=True) ]
        END_SCREEN._WON = End_Screen(game_won = True, buttons= BUTTONS)
        END_SCREEN._LOST = End_Screen(game_won = False, buttons= BUTTONS)

    @staticmethod
    def get_end_screen():
        if Global_State.game_state.game_won:
            return END_SCREEN._WON
        else:
            return END_SCREEN._LOST


class SCREEN_HANDLER:
    @staticmethod
    def start_new_game():
        _handler = Screen_Handler()
        _handler.start_new_game()



