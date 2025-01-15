import pygame

class COLOR:
    BACKGROUND = (133, 128, 121)

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
        "goblin": {"name": "Goblin", "health": 1, "image_path": "images/monsters/goblin.png"},
        # "goblin": {"name": "Goblin", "health": 1, "image_path": "images/face.png"},
        "orc": {"name": "Orc", "health": 2, "image_path": "images/monsters/orc.png"},
        # "orc": {"name": "Orc", "health": 2, "image_path": "images/face.png"},
        "troll": {"name": "Troll", "health": 3, "image_path": "images/monsters/troll.png"}
        # "troll": {"name": "Troll", "health": 3, "image_path": "images/face.png"}
    }
    
    DIAGONAL_SIZE = 0

    @staticmethod
    def initialize():
        image_path = MONSTER.MONSTER_TEMPLATES["goblin"]["image_path"]

        image = pygame.image.load(image_path).convert_alpha()
        image_width, image_height = image.get_size()

        # Scale image considering the maximum size after rotation
        MONSTER.DIAGONAL_SIZE = (image_width**2 + image_height**2) ** 0.5

class MONSTER_DECK:
    TOTAL_MONSTERS = 30

class CARD:
    SCALE = 50
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

    BETWEEN_DISTANCE = 30

class GAME_STATE:
    NUM_DRAW_MONSTERS = 2
    NUM_CARDS = 6
# class GAME_STATE:
#     game_state = None
#
#     @staticmethod
#     def initialize():
#         game_state = Game_State()

# class GAME_WINDOW:
    # GAME_WINDOW = Game_Window()
