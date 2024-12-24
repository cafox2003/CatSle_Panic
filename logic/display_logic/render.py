import pygame
from logic.game_logic.constants import BOARD
from logic.game_logic.constants import SCREEN

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

    # Renders an image at a location
    def render_image(self, image_path="images/tolkens.png", position=(0,0)):
        print(f"Destination: {position}")
        image = pygame.image.load(image_path)
        image_width, image_height = image.get_size()

        # # Calculate the top-left position for rendering
        render_position = (
            position[0] - image_width // 2,
            position[1] - image_height // 2,
        )
        # image = pygame.image.load(image_path)
        self.game_window.screen.blit(image, render_position)

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
        # self.game_window.screen.blit(transformed_image, (25, 25))
        self.game_window.screen.blit(transformed_image, (0, 0))

    # Board logic
    def render_board(self, board):
        for shape in board.shapes:
            center_x = (SCREEN.LENGTH - BOARD.LENGTH) // 2
            center_y = (SCREEN.HEIGHT - BOARD.HEIGHT) // 2
            shape(self.game_window.screen, center_x, center_y)
        print(f"Center x: {self.game_window.screen.get_width()}, center y: {self.game_window.screen.get_height()}")


    def render_monster(self, monster):
        # Load image
        image = pygame.image.load(monster.image_path).convert_alpha()
        image_width, image_height = image.get_size()

        # Scale image
        scale_factor = BOARD.RING_DISTANCE / max(image_width, image_height)
        new_width = int(image_width * scale_factor)
        new_height = int(image_height * scale_factor)
        image = pygame.transform.scale(image, (new_width, new_height))

        # Rotate the image to the default location
        rotated_image = pygame.transform.rotate(image, 270 -monster.coordinate.angle)

        #Center the image coordinate to the middle of the image
        rotated_width, rotated_height = rotated_image.get_size()
        render_position = (
            monster.coordinate.position[0] - rotated_width // 2,
            monster.coordinate.position[1] - rotated_height // 2,
        )

        #Render the image
        self.game_window.screen.blit(rotated_image, render_position)
