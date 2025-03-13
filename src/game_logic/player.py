import random
from card.deck import Deck

class Player:
    def __init__(self, full_deck, discard, player_location = "bottom"):
        self.hand_cards = []
        self.deck = None

        self.player_location = player_location

        self.load_hand(full_deck, discard)


    def load_hand(self, full_deck, discard, num_cards=6): #Add into a constant
        # hand = []
        cards_needed = num_cards - len(self.hand_cards)

        # Add the the card to the hand, and remove from the hand
        for _ in range(cards_needed):
            if full_deck:
                new_card = full_deck.pop() 
            else:
                random.shuffle(discard)
                
                full_deck = discard
                discard = []

                new_card = full_deck.pop()

            self.hand_cards.append(new_card)

        # self.hand_cards = hand
        self.deck = Deck(self.hand_cards, self.player_location)

    def remove_card(self, discard, card_to_remove = None):
        removed_card = self.deck.remove_card(card_to_remove)
        if removed_card != None:
            discard.append(removed_card)
