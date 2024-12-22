import pygame
from logic.display_logic.render import Render
from classes.card import Card
from classes.board import Board

class Game_Window:
    def __init__(self):
        # Boiler plate code to get the pygame window running
        pygame.init()
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True
        game_render = Render(self)
        # my_card = Card(":3", "A little face", image=game_render.render_card_image("images/face.png"))
        # card_2 = Card(">:D", "An EVIL guy...", image=game_render.render_card_image("images/face.png"))
        # card_3 = Card("D:", "He's worried", image=game_render.render_card_image("images/face.png"))

        board = Board(1000,1000)
        # all_cards = [my_card, card_2, card_3]
        while run:
            game_render.render_board(board)
            # game_render.show_image_test()
            # game_render.render_deck(all_cards, 25, 25, 25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.flip()
        pygame.quit()

