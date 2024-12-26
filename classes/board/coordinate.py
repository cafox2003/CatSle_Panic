from logic.game_logic.constants import BOARD, SCREEN
from classes.board.shape import get_hex_points, get_angle

class Coordinate:
    def __init__(self, ring, number, color=None):
        self.ring = ring
        self.number = number
        self.color = color
        self.angle = 0
        self.position = self.calculate_position()

    def calculate_position(self):
        MIDDLE = 2
        
        #Hex size may be different than the ring size, so it's calculated separately
        if self.ring == BOARD.RINGS[0]:
            magnitude = BOARD.HEXAGON_DISTANCE // MIDDLE
        else:
            magnitude = BOARD.HEXAGON_DISTANCE + BOARD.RINGS.index(self.ring)*BOARD.RING_DISTANCE - BOARD.RING_DISTANCE//MIDDLE

        position = get_hex_points(magnitude, 30)[(((self.number+3) % 6))] #Logic to put numbers in the right order
        self.angle = (int) (get_angle(position))
        return self.center_position(position)

    # Center the piece according to the screen size
    def center_position(self, position):
        new_x = (SCREEN.LENGTH - BOARD.LENGTH) // 2 + position[0] + BOARD.LENGTH // 2 
        new_y = (SCREEN.HEIGHT - BOARD.HEIGHT) // 2 + position[1] + BOARD.HEIGHT // 2 
        new_position = (new_x, new_y)

        return new_position

