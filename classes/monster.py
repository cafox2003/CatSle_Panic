import pygame
import random

from classes.board.coordinate import Coordinate
from logic.game_logic.constants import BOARD, MONSTER, SCREEN

class Monster:
    def __init__(self, name, health, image_path="images/default_image.png", event="none", number=1):
        self.name = name 
        self.health = health 
        self.max_health = health 
        self.image = self.render_image(image_path) 
        self.event = event 

        self.coordinate = Coordinate(BOARD.RINGS[-1], number) # start off in the forest ring
        self.angle_mod = 0 

    @classmethod
    def create_from_template(cls, template_name, number = 1):
            template = MONSTER.MONSTER_TEMPLATES[template_name]
            return cls(name = template['name'], health = template['health'], 
                       image_path = template['image_path'], number = number)

    def move(self):
        self.coordinate.move()

    @staticmethod
    def generate_monsters(num_monsters=20):
        monsters = []
        for i in range(num_monsters):
            # Number it starts at
            number = random.randint(1, 6)
            # Get a random monster type from the templates
            monster_type = random.choice(list(MONSTER.MONSTER_TEMPLATES.keys()))
            # Create a random monster and add to the list
            monsters.append(Monster.create_from_template(
                template_name =monster_type,
                number=number
            ))
        return monsters


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
        # Rotate the image to the correct angle based on the coordinate and angle_mod
        rotated_image = pygame.transform.rotate(self.image, 270 - self.coordinate.angle - self.angle_mod)

        # Get the size of the rotated image
        rotated_width, rotated_height = rotated_image.get_size()

        # Calculate the new position to ensure the image is centered at the monster's coordinates

        if self.health == self.max_health:
            render_position = (
                self.coordinate.position[0] - rotated_width // 2,
                self.coordinate.position[1] - rotated_height // 2
            )
        else:
            render_position = (
                self.coordinate.position[0] - (rotated_width // 2 + rotated_width // 5),
                self.coordinate.position[1] - (rotated_height // 2 + rotated_height // 5)
            )

        # Render the rotated image at the calculated position
        SCREEN.screen.blit(rotated_image, render_position)

    def damage(self):
        self.health -= 1

        if self.health == 0:
            pass

        self.angle_mod = (self.max_health - self.health)*120

if __name__ == "__main__":
    my_monster = Monster.create_from_template("troll")

    print(my_monster.health)

