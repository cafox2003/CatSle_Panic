import random

from logic.game_logic.constants import DECK, CARD, BOARD
from classes.card.card import Card
from classes.warrior import Warrior


class Deck:
    def __init__(self, cards, position, x=None, y=None):
        self.cards = cards
        self.position = position
        self.x = x
        self.y = y

        if self.x == None:
            self.x = DECK.DECK_MIDPOINT
        if self.y == None:
            if self.position == "top":
                self.y = DECK.TOP_DECK_POS
            elif self.position == "bottom":
                self.y = DECK.BOTTOM_DECK_POS
            else:
                raise ValueError('Deck position must be set to "top" or "bottom"')

        self.deck_width = (len(self.cards) * CARD.CARD_WIDTH) + ((len(self.cards) - 1) * DECK.BETWEEN_DISTANCE)
    def render(self):
        if not self.cards:
            return
            
        # Adjust x to align the midpoint of the deck with the calculated x
        start_x = self.x - (self.deck_width // 2)
        
        # Render each card
        for c in self.cards:
            c.render(start_x, self.y)
            start_x += (CARD.CARD_WIDTH + DECK.BETWEEN_DISTANCE)

    # Method to load all cards in the game. Maybe move into a different file
    @staticmethod
    def load_all_cards():
        # Skip the forest and castle ring
        all_warriors = []

        for ring in BOARD.RINGS[1:-1]: 
            for color in BOARD.SEGMENT_COLOR_NAMES:
                for i in range(3):
                    all_warriors.append(Warrior(ring, color))
            all_warriors.append(Warrior(ring, "any_color"))


        for color in BOARD.SEGMENT_COLOR_NAMES:
            all_warriors.append(Warrior("hero", color))

        all_cards = [warrior.card for warrior in all_warriors]

        random.shuffle(all_cards)
        return all_cards

