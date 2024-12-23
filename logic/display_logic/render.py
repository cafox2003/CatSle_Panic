import pygame
from logic.game_logic.constants import BOARD

class Render:
    def __init__(self, game_window):

        self.game_window = game_window
        self.SCALE = 100
        self.CARD_AR = (2,3) # Card aspect ratio
        self.Y_DISPLACE = 20 # Distance from the top of text
        self.CARD_WIDTH = self.CARD_AR[0] * self.SCALE
        self.CARD_HEIGHT = self.CARD_AR[1] * self.SCALE

        self.FONT_TYPE = 'arial'
        self.FONT_SIZE = 20
        self.FONT = pygame.font.SysFont(self.FONT_TYPE, self.FONT_SIZE)
        self.BLACK = (0, 0, 0)
    # CARD LOGIC
    def render_card(self, card, x, y):
        # Display image
        self.game_window.screen.blit(card.image, (x, y))

        # Display card name 
        text = self.FONT.render(card.name, True, self.BLACK)
        #Place the text at the bottom
        text_rect = text.get_rect(center=(x + self.CARD_WIDTH  // 2, y + self.Y_DISPLACE))
        self.game_window.screen.blit(text, text_rect)

        # Display card name
        text = self.FONT.render(card.description, True, self.BLACK)
        #Place the text at the bottom
        text_rect = text.get_rect(center=(x + self.CARD_WIDTH // 2, y + self.CARD_HEIGHT - self.Y_DISPLACE))
        self.game_window.screen.blit(text, text_rect)

    def render_card_image(self, image_path):
        raw_image = pygame.image.load(image_path)
        image = pygame.transform.scale(raw_image, (self.CARD_WIDTH, self.CARD_HEIGHT))
        return image

    def render_deck(self, cards, x, y, distance):
        for c in cards:
            self.render_card(c, x, y)
            x += (distance + self.CARD_WIDTH)

    # Logic to display images
    def show_image_test(self, image_path="images/sword_man.jpg"):
        image = pygame.image.load(image_path)

        transformed_image = pygame.transform.scale(image, (2*self.SCALE, 3*self.SCALE))
        self.game_window.screen.blit(transformed_image, (25, 25))


    # Board logic
    def render_board(self, board):
        for shape in board.shapes:
            center_x = (self.game_window.screen.get_width() - BOARD.LENGTH) // 2
            center_y = (self.game_window.screen.get_height() - BOARD.HEIGHT) // 2
            shape(self.game_window.screen, center_x, center_y)
