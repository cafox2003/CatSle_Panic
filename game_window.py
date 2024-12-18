import pygame

class Game_Window:
    def __init__(self):
        # Boiler plate code to get the pygame window running
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))


        self.player = pygame.Rect((300, 250, 50, 50))
        # Run the main loop
        self.main_loop()

    def main_loop(self): #Maybe change name
        run = True
        while run:

            pygame.draw.rect(self.screen, (255,0,0), self.player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()


        pygame.quit()


