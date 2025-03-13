import random
from game_logic.constants import DECK, CARD, BOARD
from card.warrior_card import Warrior_Card


class Deck:
    def __init__(self, cards, position, x=None, y=None):
        self.cards = cards
        self.active_card = None

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
                    all_warriors.append(Warrior_Card(ring, color))
            all_warriors.append(Warrior_Card(ring, "any_color"))

        # Add the hero cards for every color
        for color in BOARD.SEGMENT_COLOR_NAMES:
            all_warriors.append(Warrior_Card("hero", color))

        all_cards = [warrior for warrior in all_warriors]

        random.shuffle(all_cards)
        return all_cards

    def check_card_click(self, mouse_pos):
        for card in self.cards:
            if card.check_click(mouse_pos):
                self.active_card = card
                return card  # Return the clicked card
        return None  # No card clicked

    # Remove the active card
    def remove_card(self, card_to_remove = None ):
        if card_to_remove == None:
           card_to_remove = self.active_card

        self.cards.remove(card_to_remove)

        return card_to_remove
