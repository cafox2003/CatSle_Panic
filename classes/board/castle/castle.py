import pygame
import random
from classes.board.shape import Shape, get_hex_points
from logic.game_logic.constants import BOARD

class Castle:
    def __init__(self, number, radius):
        self.destroyed = False
        self.number = number

        self.shape = self.get_shape(radius)
    def get_shape(self, radius):

        line_hex_points = get_hex_points(radius, 60) 

        start_point = line_hex_points[(self.number + 2) % 6]
        end_point = line_hex_points[(self.number + 3) % 6]

        line = Shape(
                shape_type="line",
                color = BOARD.WALL_COLOR,
                pos_start = start_point,
                pos_end = end_point,
                centered=True,
                border_width = BOARD.HEX_BORDER_WIDTH
            )
        return line.get_draw_function()
