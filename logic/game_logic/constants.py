# class Rings(self):
#     KNIGHT

class SCREEN:
    LENGTH = 1920
    HEIGHT = 1080

class BOARD:
    LENGTH = 1000
    HEIGHT = LENGTH
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

class MONSTER:
    MONSTER_TEMPLATES = {
        "goblin": {"name": "Goblin", "health": 1, "image_path": "images/monsters/goblin.png"},
        "orc": {"name": "Orc", "health": 2, "image_path": "images/monsters/orc.png"},
        "troll": {"name": "Troll", "health": 3, "image_path": "images/monsters/troll.png"}
    }
