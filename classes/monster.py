import pygame

from classes.board.coordinate import Coordinate
from logic.game_logic.constants import BOARD, MONSTER, SCREEN

class Monster:
    #TODO: Make default_image.png
    def __init__(self, name, health, image_path="images/default_image.png", event="none", number=1):
        self.name = name 
        self.health = health 
        self.max_health = health 
        # self.image_path = image_path 
        self.image = self.render_image(image_path) 
        self.event = event 

        self.coordinate = Coordinate(BOARD.RINGS[-1], number) # start off in the forest ring

    @classmethod
    def create_from_template(cls, template_name, number = 1):
            template = MONSTER.MONSTER_TEMPLATES[template_name]
            return cls(name = template['name'], health = template['health'], 
                       image_path = template['image_path'], number = number)
    @staticmethod
    def render_image(image_path):
        # Load image
        image = pygame.image.load(image_path).convert_alpha()
        image_width, image_height = image.get_size()

        # Scale image
        scale_factor = BOARD.RING_DISTANCE / max(image_width, image_height)
        new_width = int(image_width * scale_factor)
        new_height = int(image_height * scale_factor)
        image = pygame.transform.scale(image, (new_width, new_height))

        return image

    def render(self):
        # Rotate the image to the default location
        # TODO: Define angle by the monster's health
        rotated_image = pygame.transform.rotate(self.image, 270 -self.coordinate.angle)

        #Center the image coordinate to the middle of the image
        rotated_width, rotated_height = rotated_image.get_size()
        render_position = (
            self.coordinate.position[0] - rotated_width // 2 + BOARD.X_DISPLACEMENT,
            self.coordinate.position[1] - rotated_height // 2 + BOARD.Y_DISPLACEMENT,
        )

        #Render the image
        SCREEN.screen.blit(rotated_image, render_position)

if __name__ == "__main__":
    my_monster = Monster.create_from_template("troll")

    print(my_monster.health)

