from logic.game_logic.constants import SCREEN, END_SCREEN
from logic.game_logic.global_state import Global_State 
from logic.display_logic.button import Button
from logic.display_logic.menu_screen import Menu_Screen

class End_Screen(Menu_Screen):

    def __init__(self, game_won):

        if game_won:
            message = END_SCREEN.OUTCOME_MESSAGES["won"]
        else:
            message = END_SCREEN.OUTCOME_MESSAGES["lost"]

        buttons = [
            Button(SCREEN.LENGTH // 2, SCREEN.HEIGHT * 3//4, 150, 50, "Restart game", Global_State.game_state.reset, centered=True), # Move button
                ]
        super().__init__(message, buttons)
