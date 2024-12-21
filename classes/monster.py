monster_templates = {
    "goblin": {"name": "Goblin", "health": 1},
    "orc": {"name": "Orc", "health": 2},
    "troll": {"name": "Troll", "health": 3}
}

class Monster:
    #TODO: Make default_image.png
    def __init__(self, name, health, image="images/default_image.png", event="none"):
        self.name = name # Name of the monster
        self.health = health # Current health
        self.max_health = health # The max health it can have
        self.image = image #An image file for the monster
        self.event = event #If it triggers a special event (plague, boss, move all, draw more, ect...) 

        self.location = -1 # The location from 1-6 they're in. USE THE SPECIALIZED COORDINATE OBJ
        self.ring = 0 # The ring they're in (archer, knight, sword, castle) 

    @classmethod
    def create_from_template(cls, template_name):
            template = monster_templates[template_name]
            return cls(template['name'], template['health'])

if __name__ == "__main__":
    my_monster = Monster.create_from_template("troll")

    print(my_monster.health)

