# Contains "scraps" of code used for testing game_window

        # my_card = Card(":3", "A little face", image=game_render.render_card_image("images/face.png"))
        # card_2 = Card(">:D", "An EVIL guy...", image=game_render.render_card_image("images/face.png"))
        # card_3 = Card("D:", "He's worried", image=game_render.render_card_image("images/face.png"))
        # all_cards = [my_card, card_2, card_3]


        # game_render.show_image_test()
        # game_render.render_deck(all_cards, 25, 25, 25)
                # game_render.render_card(my_card, my_coord.position[0], my_coord.position[1])

# # Render board
# board = Board()
# board.render()
#
# # Render monsters
# # monsters = [Monster.create_from_template("orc", i) for i in range(1,7)]
# all_monsters = Monster.generate_monsters()
# current_monsters = []
#
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     # Update the screen
#     SCREEN.screen.fill((0,0,0))
#     board.render()
#
#     current_monsters.append(all_monsters.pop())
#
#     for monster in current_monsters:
#         monster.render()
#         monster.move()
#     time.sleep(1)
#
#     if len(all_monsters) == 0:
#         run = False
#
#     pygame.display.flip()
# pygame.quit()
