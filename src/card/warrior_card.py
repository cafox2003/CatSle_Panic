from card.card import Card

class Warrior_Card(Card):
    def __init__(self, ring, color):
        self.ring = ring.lower()
        self.color = color.lower()
        self.name = f"{color} {ring}".title()

        description = f"Hit 1 monster in {self.name} ring"
        image_path = f"../images/cards/battle/{self.ring}/{self.color}.png"

        super().__init__("Warrior", "", "", image_path)

