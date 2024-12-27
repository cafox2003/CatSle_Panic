from classes.card.card import Card

class Warrior:
    def __init__(self, ring, color):
        self.ring = ring.lower()
        self.color = color.lower()
        self.name = f"{ring} {color}".title()

        description = f"Hit 1 monster in {self.name} ring"
        image_path = f"images/cards/battle/{self.ring}/{self.color}.png"

        self.card = Card("", "", image_path) # No name/description needed for cards it's written on

