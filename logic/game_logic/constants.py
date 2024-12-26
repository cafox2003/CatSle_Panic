import pygame

class SCREEN:
    LENGTH = 1920
    HEIGHT = 1080
    screen = None

    @staticmethod
    def initialize():
        SCREEN.screen = pygame.display.set_mode((SCREEN.LENGTH, SCREEN.HEIGHT))

class BOARD:
    # Border that the board will be surrounded with. Number of pixels
    BOARD_BORDER = 60

    # LENGTH = 1000
    # HEIGHT = LENGTH

    HEIGHT = SCREEN.HEIGHT - 2*BOARD_BORDER
    LENGTH = HEIGHT

    RINGS = ["Castle", "Swordsman", "Knight", "Archer", "Forest"]

    RING_DISTANCE = (int) (LENGTH // 10.5) # Roughly the constant needed for the rings to be correctly sized (according to the text)
    HEXAGON_DISTANCE = (int) (RING_DISTANCE* 1.25)

    TEXT_COLOR = (255,255,255)
    BORDER_COLOR = (0,0,0)
    SEGMENT_COLORS = [(255,0,0),(0,255,0),(0,0,255)]
    CASTLE_COLOR = (100, 100, 100)
    FOREST_COLOR = (63, 117, 57)
    BOARD_COLOR = (118, 168, 96)

    RING_FONT_SIZE = LENGTH // 20
    NUMBER_FONT_SIZE = LENGTH // 11

    # Middle of the screen
    X_MID = (SCREEN.LENGTH ) // 2
    Y_MID = (SCREEN.HEIGHT ) // 2

    # Offset of the board
    X_OFFSET = LENGTH//2 + BOARD_BORDER
    Y_OFFSET = Y_MID

    # Add these constants to anything you wish to render on the board
    X_DISPLACEMENT = X_OFFSET - X_MID
    Y_DISPLACEMENT = Y_OFFSET - Y_MID

class MONSTER:
    MONSTER_TEMPLATES = {
        "goblin": {"name": "Goblin", "health": 1, "image_path": "images/monsters/goblin.png"},
        "orc": {"name": "Orc", "health": 2, "image_path": "images/monsters/orc.png"},
        "troll": {"name": "Troll", "health": 3, "image_path": "images/monsters/troll.png"}
    }

class CARD:
    SCALE = 100
    CARD_AR = (2,3) # Card aspect ratio
    Y_DISPLACE = 20 # Distance from the top of text
    CARD_WIDTH = CARD_AR[0] * SCALE
    CARD_HEIGHT = CARD_AR[1] * SCALE

    FONT_TYPE = 'arial'
    FONT_SIZE = 20
    # FONT = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)
    # FONT = None
    BLACK = (0, 0, 0)

# class GAME_WINDOW:
    # GAME_WINDOW = Game_Window()
