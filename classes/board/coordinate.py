from logic.game_logic.constants import BOARD, SCREEN, MONSTER
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

        # magnitude -= MONSTER.DIAGONAL_SIZE // 2

        position = get_hex_points(magnitude, 30)[(((self.number+3) % 6))] #Logic to put numbers in the right order
        self.angle = (int) (get_angle(position))
        return self.center_position(position)

    # Center the piece according to the screen size
    def center_position(self, position):
        new_x = BOARD.X_OFFSET + position[0]
        new_y = BOARD.Y_OFFSET + position[1]
        new_position = (new_x, new_y)
        return new_position
    
    # Moves the coordinate forward
    def move(self):
        if self.ring == BOARD.RINGS[0]:
            self.number = self.next_number(self.number) # Move clockwise around the castle ring
        else:
            self.ring = BOARD.RINGS[BOARD.RINGS.index(self.ring)-1] # Move one ring inward

        self.position = self.calculate_position()

    # Returns the next (clockwise) number.
    @staticmethod
    def next_number(index):
        # TODO: 6 comes from there being 6 rings. Change this and every similar usage to us a constant
        return ((index % 6) + 1) 
