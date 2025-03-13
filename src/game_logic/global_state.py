from game_logic.game_state import Game_State

class Global_State:
    game_state = None  # Class-level variable to store the game state

    @staticmethod
    def initialize():
        Global_State.game_state = Game_State()  # Assign to the class variable
        # if Global_State.game_state is None:  # Ensure it only initializes once
        #     Global_State.game_state = Game_State()  # Assign to the class variable
        # else:
        #     print("Game state already initialized!")
