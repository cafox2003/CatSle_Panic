from logic.game_logic.constants import BOARD 
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
        self.position = None

        self.calculate_position()

    def calculate_position(self, num_monsters = 1, monster_pos = 1):

        MIDDLE = 2
        
        #Hex size may be different than the ring size, so it's calculated separately
        if self.ring == BOARD.RINGS[0]:
            magnitude = BOARD.HEXAGON_DISTANCE // MIDDLE
        else:
            magnitude = BOARD.HEXAGON_DISTANCE + BOARD.RINGS.index(self.ring.title())*BOARD.RING_DISTANCE - BOARD.RING_DISTANCE//MIDDLE


        angle_offset = self.get_angle_offset(num_monsters, monster_pos) # Get the offset based on how many monsters are on the same spot

        position = get_hex_points(magnitude, angle_offset)[(self.number + 3) % BOARD.NUM_SEGMENTS]  # Uses hexagon logic + offset to get the correct point
        self.angle = (int) (get_angle(position))

        self.position = self.center_position(position)

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
    def move(self, num_monsters = 1, monster_pos = 1, is_forward = True):
        # TODO: Remove instances of .lower() and instead store "BOARD.INTERNAL_RINGS" as lowercase rings
        if is_forward:
            if self.ring == BOARD.RINGS[0].lower():  # Ensure consistent comparison for the castle ring
                self.number = self.next_number(self.number)  # Move clockwise around the castle ring
            else:
                # Move one ring inward
                self.ring = self.next_ring()
        else: # If moving backward
                # Move one ring backward
            self.ring = self.previous_ring()

        self.position = self.calculate_position(num_monsters = num_monsters, monster_pos = monster_pos)
        self.set_color()  # Recalculate color after updating ring and position

    # Returns the next (clockwise) number.
    @staticmethod
    def next_number(index):
        return ((index % BOARD.NUM_SEGMENTS) + 1) 

    # Returns the previous number (so counter clockwise)
    @staticmethod
    def previous_number(index):
        return (BOARD.NUM_SEGMENTS - index+ 1)

    # Return the next ring
    def next_ring(self):
        ring_index = BOARD.RINGS.index(self.ring.title())
        if ring_index > 0:
            return BOARD.RINGS[ring_index - 1].lower()
        else:
            return BOARD.RINGS[0].lower() #Don't circle back to forest ring

    # Return the previous ring
    def previous_ring(self):
        ring_index = BOARD.RINGS.index(self.ring.title())

        if ring_index >= (len(BOARD.RINGS) -1):
            previous_ring_index = ring_index
        else:
            previous_ring_index = ring_index + 1
            
        return BOARD.RINGS[previous_ring_index].lower()
