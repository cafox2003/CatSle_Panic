import pygame
from logic.display_logic.render import Render

class Card:
    def __init__(self, name, description, image):

        self.name = name # Name of the card
        self.description = description 
        
        self.image = image
        
if __name__ == "__main__":
    my_card = Card(":3", "A little face", image="../images/face.png")

    print(my_card.description)
