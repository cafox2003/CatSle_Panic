from board.shape import Shape, get_hex_points
from game_logic.constants import BOARD

class Castle:
    def __init__(self, number, radius):
        self.destroyed = False
        self.number = number

        self.shape = self.get_shape(radius)
    def get_shape(self, radius):

        CIRCLE = 360
        angle_inc = CIRCLE // BOARD.NUM_SEGMENTS 

        line_hex_points = get_hex_points(radius, angle_inc) 

        start_point = line_hex_points[(self.number + 2) % BOARD.NUM_SEGMENTS]
        end_point = line_hex_points[(self.number + 3) % BOARD.NUM_SEGMENTS]

        line = Shape(
                shape_type="line",
                color = BOARD.WALL_COLOR,
                pos_start = start_point,
                pos_end = end_point,
                centered=True,
                border_width = BOARD.HEX_BORDER_WIDTH
            )
        return line.get_draw_function()
