from logic.game_logic.constants import BOARD, SCREEN, MONSTER
from classes.board.shape import get_hex_points, get_angle

# from classes.monster.monster_deck import Monster_Deck
# from logic.game_logic.global_state import Global_State 

class Coordinate:
    def __init__(self, ring, number):
        self.ring = ring.lower()
        self.number = number

        self.color = self.get_color(self.number).lower()

        self.set_color() # Sets color based on the number
        self.angle = 0
        self.position = self.calculate_position()

    def calculate_position(self, num_monsters = 1, monster_pos = 1):

        MIDDLE = 2
        
        #Hex size may be different than the ring size, so it's calculated separately
        if self.ring == BOARD.RINGS[0]:
            magnitude = BOARD.HEXAGON_DISTANCE // MIDDLE
        else:
            magnitude = BOARD.HEXAGON_DISTANCE + BOARD.RINGS.index(self.ring.title())*BOARD.RING_DISTANCE - BOARD.RING_DISTANCE//MIDDLE


        angle_offset = self.get_angle_offset(num_monsters, monster_pos) # Get the offset based on how many monsters are on the same spot

        position = get_hex_points(magnitude, angle_offset)[(self.number + 3) % 6]  # Uses hexagon logic + offset to get the correct point
        self.angle = (int) (get_angle(position))
        return self.center_position(position)

    # Center the piece according to the screen size
    def center_position(self, position):
        new_x = BOARD.X_OFFSET + position[0]
        new_y = BOARD.Y_OFFSET + position[1]
        new_position = (new_x, new_y)
        return new_position

    # Returns the angle offset that the piece should have
    @staticmethod
    def get_angle_offset(num_monsters = 1, monster_pos = 1):
        return (int) (60 * (monster_pos)/(num_monsters+1))



    # Return the color segment based on the number
    @staticmethod
    def get_color(number):
        index = ((number - 1) // 2 + 1) % 3 
        return BOARD.SEGMENT_COLOR_NAMES[index]

    def set_color(self):
        # print(f"Old color: {self.color}")
        self.color = self.get_color(self.number).lower()
        # print(f"New color: {self.color}\n\n")

    
    # Moves the coordinate forward
    def move(self, num_monsters = 1, monster_pos = 1):
        # TODO: Remove instances of .lower() and instead store "BOARD.INTERNAL_RINGS" as lowercase rings
        if self.ring == BOARD.RINGS[0].lower():  # Ensure consistent comparison for the castle ring
            self.number = self.next_number(self.number)  # Move clockwise around the castle ring
        else:
            # Move one ring inward
            ring_index = BOARD.RINGS.index(self.ring.title())
            self.ring = BOARD.RINGS[ring_index - 1].lower()

        self.position = self.calculate_position(num_monsters = num_monsters, monster_pos = monster_pos)
        self.set_color()  # Recalculate color after updating ring and position

    # Returns the next (clockwise) number.
    @staticmethod
    def next_number(index):
        # TODO: 6 comes from there being 6 rings. Change this and every similar usage to us a constant
        return ((index % 6) + 1) 
