from game_logic.constants import BOARD
from .castle import Castle

class Wall(Castle):
    def __init__(self, number):
        super().__init__(number, BOARD.HEXAGON_DISTANCE)
