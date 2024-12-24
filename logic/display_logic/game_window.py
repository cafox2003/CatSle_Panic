import pygame
from logic.display_logic.render import Render
from classes.card import Card
from classes.board.board import Board
from classes.board.coordinate import Coordinate
from classes.monster import Monster
from logic.game_logic.constants import SCREEN, BOARD



class Game_Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN.LENGTH, SCREEN.HEIGHT))

        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True
        game_render = Render(self)
        my_card = Card(":3", "A little face", image=game_render.render_card_image("images/face.png"))
        # card_2 = Card(">:D", "An EVIL guy...", image=game_render.render_card_image("images/face.png"))
        # card_3 = Card("D:", "He's worried", image=game_render.render_card_image("images/face.png"))
        # all_cards = [my_card, card_2, card_3]

        board = Board()



        game_render.render_board(board)

        my_monster = Monster.create_from_template("goblin", 3)

        game_render.render_monster(my_monster)
        # for ring in BOARD.RINGS:
        #     for i in range(1, 7):
        #         my_coord = Coordinate(ring, i)
        #         print(f"Destination: {my_coord.position}, Angle: {my_coord.angle}")
        #         game_render.render_tolken(image_path="images/tolkens.png", coordinate = my_coord)


        while run:
            # game_render.show_image_test()
            # game_render.render_deck(all_cards, 25, 25, 25)
                    # game_render.render_card(my_card, my_coord.position[0], my_coord.position[1])


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.flip()
        pygame.quit()

