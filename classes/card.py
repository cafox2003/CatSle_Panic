import pygame
from logic.display_logic.render import Render
from logic.game_logic.constants import SCREEN, CARD

class Card:
    def __init__(self, name, description, image_path):
        self.name = name 
        self.description = description 
        self.image = self.render_image(image_path)
        
    def render(self, x, y):

        FONT = pygame.font.SysFont(CARD.FONT_TYPE, CARD.FONT_SIZE)

        # Display image
        SCREEN.screen.blit(self.image, (x, y))

        # Display card name 
        text = FONT.render(self.name, True, CARD.BLACK)
        #Place the text at the bottom
        text_rect = text.get_rect(center=(x + CARD.CARD_WIDTH  // 2, y + CARD.Y_DISPLACE))
        SCREEN.screen.blit(text, text_rect)

        # Display card name
        text = FONT.render(self.description, True, CARD.BLACK)
        #Place the text at the bottom
        text_rect = text.get_rect(center=(x + CARD.CARD_WIDTH // 2, y + CARD.CARD_HEIGHT - CARD.Y_DISPLACE))
        SCREEN.screen.blit(text, text_rect)

    @staticmethod
    def render_image(image_path):
        raw_image = pygame.image.load(image_path)
        image = pygame.transform.scale(raw_image, (CARD.CARD_WIDTH, CARD.CARD_HEIGHT))
        return image

    # NOT TESTED
    @staticmethod
    def render_deck(cards, x, y, distance):
        for c in cards:
            self.render(c, x, y)
            x += (distance + CARD.CARD_WIDTH)

if __name__ == "__main__":
    my_card = Card(":3", "A little face", image="../images/face.png")
    print(my_card.description)
