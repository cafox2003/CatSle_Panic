from game_logic.constants import  END_SCREEN
from display_logic.menu_screen import Menu_Screen

class End_Screen(Menu_Screen):

    def __init__(self, game_won, buttons):

        if game_won:
            message = END_SCREEN.OUTCOME_MESSAGES["won"]
        else:
            message = END_SCREEN.OUTCOME_MESSAGES["lost"]

        super().__init__(message, buttons)
