class Screen_Handler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Screen_Handler, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.current_screen = None
            self.initialize()

    def initialize(self):
        # Initialize shared resources
        from logic.game_logic.constants import initialize
        from logic.game_logic.global_state import Global_State
        from logic.display_logic.gui_constants import END_SCREEN

        initialize()
        Global_State.initialize()
        END_SCREEN.initialize()

        # Start the game
        self.start_new_game()

    def start_new_game(self):
        from logic.display_logic.game_window import Game_Window
        self.current_screen = Game_Window()

    def display_menu(self):
        # Add logic for displaying a menu screen
        pass

    def display_end_screen(self):
        from logic.display_logic.gui_constants import END_SCREEN
        self.current_screen = END_SCREEN.get_end_screen()
        self.current_screen.display()
