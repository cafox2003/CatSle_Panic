import pygame
from logic.game_logic.constants import BOARD
from logic.game_logic.constants import SCREEN

class Render:
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
        SCREEN.screen.blit(image, render_position)

    # Logic to display images
    def show_image_test(self, image_path="images/sword_man.jpg"):
        image = pygame.image.load(image_path)
        transformed_image = pygame.transform.scale(image, (2*self.SCALE, 3*self.SCALE))
        SCREEN.screen.blit(transformed_image, (0, 0))

