import pygame
from logic.game_logic.constants import SCREEN, END_SCREEN

class Menu_Screen():
    def __init__(self, message, buttons):

        self.buttons = buttons
        self.message = message

    def display(self):
        self.render()

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
        text = font.render(self.message, True, END_SCREEN.TEXT_COLOR)

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
