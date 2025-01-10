import pygame
from logic.game_logic.constants import SCREEN

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (200, 200, 200)  # Default button color
        self.hover_color = (170, 170, 170)  # Color when hovered

    def render(self):
        # Change color on hover
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(SCREEN.screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(SCREEN.screen, self.color, self.rect)
        
        # Render text on the button
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        SCREEN.screen.blit(text_surface, text_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.action()  # Call the button's action when clicked
