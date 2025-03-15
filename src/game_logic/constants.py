import pygame

def initialize():
    SCREEN.initialize()
    FONT.initialize()
    MONSTER.initialize()

class COLOR:
    BACKGROUND = (133, 128, 121)
    TEXT = (0, 0, 0)

class SCREEN:

    screen = None
    HEIGHT = 0
    LENGTH = 0

    # HEIGHT = 900
    # LENGTH = HEIGHT * 16/9

    pygame.init()

    DISPLAY_INFO = pygame.display.Info()
    DISPLAY_WIDTH, DISPLAY_HEIGHT = DISPLAY_INFO.current_w, DISPLAY_INFO.current_h

    ASPECT_RATIO = 16/9;
    # SCREEN_SCALE = 0.834
    SCREEN_SCALE = 1

    HEIGHT = (int) (DISPLAY_HEIGHT * SCREEN_SCALE)
    LENGTH = (int) (HEIGHT * ASPECT_RATIO)

    print(f"Width: {LENGTH}, height: {HEIGHT}")
    @staticmethod
    def initialize():
        SCREEN.screen = pygame.display.set_mode((SCREEN.LENGTH, SCREEN.HEIGHT))

    # @staticmethod
    # def initialize():
    #
    #     pygame.init()
    #
    #     DISPLAY_INFO = pygame.display.Info()
    #     DISPLAY_WIDTH, DISPLAY_HEIGHT = DISPLAY_INFO.current_w, DISPLAY_INFO.current_h
    #
    #
    #     ASPECT_RATIO = 16/9;
    #     SCREEN_SCALE = 0.8
    #
    #     # SCREEN.HEIGHT = DISPLAY_HEIGHT * SCREEN_SCALE
    #     # SCREEN.LENGTH = SCREEN.HEIGHT * ASPECT_RATIO
    #     SCREEN.HEIGHT = DISPLAY_HEIGHT * SCREEN_SCALE
    #     SCREEN.LENGTH = SCREEN.HEIGHT * ASPECT_RATIO
    #
    #     print(f"Width: {SCREEN.LENGTH}, height: {SCREEN.HEIGHT}")
    #     SCREEN.screen = pygame.display.set_mode((SCREEN.LENGTH, SCREEN.HEIGHT))

class BOARD:
    # Border that the board will be surrounded with. Number of pixels
    BOARD_BORDER_CONST = 30
    BOARD_BORDER = SCREEN.LENGTH // BOARD_BORDER_CONST
    HEX_BORDER_WIDTH = 6
    CIRCLE_BORDER_WIDTH = HEX_BORDER_WIDTH - 1

    VERTEX_RADIUS = HEX_BORDER_WIDTH * 4//3

    HEIGHT = SCREEN.HEIGHT - 2*BOARD_BORDER
    LENGTH = HEIGHT

    RINGS = ["Castle", "Swordsman", "Knight", "Archer", "Forest"]

    RING_DISTANCE = (int) (LENGTH // 10.5) # Roughly the constant needed for the rings to be correctly sized (according to the text)
    HEXAGON_DISTANCE = (int) (RING_DISTANCE* 1.25)
    TOWER_DISTANCE = HEXAGON_DISTANCE * 2//3

    TEXT_COLOR = (255,255,255)
    BORDER_COLOR = (0,0,0)
    SEGMENT_COLORS = [(255,0,0),(0,255,0),(0,0,255)]
    SEGMENT_COLOR_NAMES = ["Red", "Green", "Blue"]

    NUM_SEGMENTS = len(SEGMENT_COLORS) * 2

    CASTLE_COLOR = (100, 100, 100)
    WALL_COLOR = (170, 170, 170)
    # WALL_COLOR = (255,255,255)
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
        "goblin": {"name": "Goblin", "health": 1, "image_path": "../images/monsters/goblin.png"},
        # "goblin": {"name": "Goblin", "health": 1, "image_path": "images/face.png"},
        "orc": {"name": "Orc", "health": 2, "image_path": "../images/monsters/orc.png"},
        # "orc": {"name": "Orc", "health": 2, "image_path": "images/face.png"},
        "troll": {"name": "Troll", "health": 3, "image_path": "../images/monsters/troll.png"}
        # "troll": {"name": "Troll", "health": 3, "image_path": "images/face.png"}
    }
    
    DIAGONAL_SIZE = 0

    @staticmethod
    def initialize():
        image_path = MONSTER.MONSTER_TEMPLATES["goblin"]["image_path"]

        image = pygame.image.load(image_path).convert_alpha()
        image_width, image_height = image.get_size()

        scale_monster = 2

        # Scale image considering the maximum size after rotation
        MONSTER.DIAGONAL_SIZE = ((image_width**2 + image_height**2) ** 0.5)*(1/scale_monster)
        # MONSTER.DIAGONAL_SIZE = BOARD.RING_DISTANCE // scale_monster
        print(f"Monster diag size: {MONSTER.DIAGONAL_SIZE}")
        print(f"Hex size: {BOARD.HEX_BORDER_WIDTH}")

class MONSTER_DECK:
    TOTAL_MONSTERS = 30


class CARD:
    SCALE_CONST = 30
    SCALE = SCREEN.LENGTH // SCALE_CONST # Scale based on the width
    CARD_AR = (2,3) # Card aspect ratio
    Y_DISPLACE = (int) (SCALE//5) # Distance from the top of text
    CARD_WIDTH = CARD_AR[0] * SCALE
    CARD_HEIGHT = CARD_AR[1] * SCALE

    FONT_TYPE = 'arial'
    FONT_SIZE = 18
    BLACK = (0, 0, 0)

    # Constant to keep track of the midpoint the deck should be at
    DECK_MIDPOINT = SCREEN.LENGTH - ((SCREEN.LENGTH - (BOARD.BOARD_BORDER + BOARD.LENGTH)) // 2)

    TYPES = ["Warrior"]

class DECK:
    DECK_MIDPOINT = SCREEN.LENGTH - ((SCREEN.LENGTH - (BOARD.BOARD_BORDER + BOARD.LENGTH)) // 2)

    TOP_DECK_POS = (BOARD.BOARD_BORDER)
    BOTTOM_DECK_POS = (SCREEN.HEIGHT - BOARD.BOARD_BORDER - CARD.CARD_HEIGHT)

    BETWEEN_DISTANCE_CONST = 3
    BETWEEN_DISTANCE = CARD.CARD_WIDTH // BETWEEN_DISTANCE_CONST

class GAME_STATE:
    NUM_DRAW_MONSTERS = 2
    NUM_CARDS = 6


class END_SCREEN:
    OUTCOME_MESSAGES = {"won": "You have won!", "lost": "Game Over"}
    TEXT_COLOR = COLOR.TEXT  # Use the same text color or customize it
    FONT_TYPE = 'arial'
    FONT_SIZE = 64  # Larger font for the end screen
    BACKGROUND_COLOR = COLOR.BACKGROUND  # Use the default background color or customize
    DISPLAY_TIME = 3000  # Duration to display the end screen (in milliseconds)

class GAME_WINDOW:
    menu_screen = None

class FONT:
    SCALE_FACTOR = SCREEN.LENGTH // 900 # Scale the font based on the base screen size
    BUTTON = 36

    @staticmethod
    def initialize():
        FONT.BUTTON = FONT.scale(FONT.BUTTON)

    @staticmethod
    def scale(number):
        return FONT.SCALE_FACTOR * number
