# class Rings(self):
#     KNIGHT
# class Constants:
#     def __init__(self):
#         self.RINGS = ["Swordsman", "Knight", "Archer", "Forest"]

class BOARD:
    # def __init__(self):
    LENGTH = 1000
    HEIGHT = LENGTH
    RINGS = ["Swordsman", "Knight", "Archer", "Forest"]

    RING_DISTANCE = (int) (LENGTH // 10.5) # Roughly the constant needed for the rings to be correctly sized (according to the text)
    HEXAGON_DISTANCE = RING_DISTANCE* 1.25

    TEXT_COLOR = (255,255,255)
    BORDER_COLOR = (0,0,0)
    SEGMENT_COLORS = [(255,0,0),(0,255,0),(0,0,255)]
    CASTLE_COLOR = (100, 100, 100)
    FOREST_COLOR = (63, 117, 57)
    BOARD_COLOR = (118, 168, 96)

    RING_FONT_SIZE = LENGTH // 20
    NUMBER_FONT_SIZE = LENGTH // 11

