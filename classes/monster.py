from classes.board.coordinate import Coordinate
from logic.game_logic.constants import BOARD, MONSTER

class Monster:
    #TODO: Make default_image.png
    def __init__(self, name, health, image_path="images/default_image.png", event="none", number=1):
        self.name = name # Name of the monster
        self.health = health # Current health
        self.max_health = health # The max health it can have
        self.image_path = image_path #An image file for the monster
        self.event = event #If it triggers a special event (plague, boss, move all, draw more, ect...) 

        # self.location = -1 # The location from 1-6 they're in. USE THE SPECIALIZED COORDINATE OBJ
        # self.ring = 0 # The ring they're in (archer, knight, sword, castle) 

        self.coordinate = Coordinate(BOARD.RINGS[-1], number)

    @classmethod
    def create_from_template(cls, template_name, number = 1):
            template = MONSTER.MONSTER_TEMPLATES[template_name]
            return cls(name = template['name'], health = template['health'], 
                       image_path = template['image_path'], number = number)

if __name__ == "__main__":
    my_monster = Monster.create_from_template("troll")

    print(my_monster.health)

