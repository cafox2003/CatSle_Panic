import pygame
from logic.game_logic.constants import SCREEN, END_SCREEN
from logic.game_logic.global_state import Global_State 
from logic.display_logic.button import Button

class End_Screen():
    def __init__(self, game_won):
        print("In end screen")

        self.buttons = [
            Button(1500, 200, 150, 50, "Restart game", Global_State.game_state.reset), # Move button
                ]

        if game_won:
            self.message = END_SCREEN.OUTCOME_MESSAGES["won"]
        else:
            self.message = END_SCREEN.OUTCOME_MESSAGES["lost"]

    def display(self):
        self.render()
        self.check_buttons()


    def render(self):
        self.render_screen()
        self.render_buttons()

        # Update the display
        pygame.display.flip()

    def render_screen(self):
        # Fill the background
        SCREEN.screen.fill(END_SCREEN.BACKGROUND_COLOR)

        # Create the font
        font = pygame.font.SysFont(END_SCREEN.FONT_TYPE, END_SCREEN.FONT_SIZE)
        if Global_State.game_state.game_won:
            text = font.render("You Win!", True, END_SCREEN.TEXT_COLOR)
        else:
            text = font.render("You Lose!", True, END_SCREEN.TEXT_COLOR)

        # Center the text
        text_rect = text.get_rect(center=(SCREEN.LENGTH // 2, SCREEN.HEIGHT // 2))
        SCREEN.screen.blit(text, text_rect)


    def render_buttons(self):
        for button in self.buttons:
            button.render()


    def check_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.check_click(mouse_pos)
