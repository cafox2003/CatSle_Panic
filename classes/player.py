from classes.card.deck import Deck

class Player:
    def __init__(self, deck, discard, player_location = "bottom"):
        self.hand = self.load_hand(deck, discard)
        self.deck = Deck(self.hand, player_location)

    @staticmethod
    def load_hand(deck, discard, num_cards=6): #Add into a constant
        hand = []

        # Add the the card to the hand and discard, and remove from the hand
        for _ in range(num_cards):
            new_card = deck.pop() 

            hand.append(new_card)
            discard.append(new_card)

        return hand
