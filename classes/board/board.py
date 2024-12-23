import pygame
import pygame.gfxdraw
import math
from classes.board.shape import Shape, get_hex_points


from logic.game_logic.constants import BOARD

class Board:
    def __init__(self):
        #TODO: Add/load all colors, fonts, and font size as constants
        self.shapes = []

        self.create_shapes()

    def add_shape(self, shape_type, color, relative_position=(0, 0), border_width=0, width=0, height=0, radius=0, 
                 angle_start=0, angle_end=0, pos_start=(0,0), pos_end=(0,0), points=[], text="", font_size=0, centered=False):
        shape = Shape(shape_type, color, relative_position, border_width, width, height, radius, angle_start, angle_end,
                      pos_start, pos_end, points, text, font_size, centered)

        draw_function = shape.get_draw_function(BOARD.LENGTH, BOARD.HEIGHT)
        self.shapes.append(draw_function)

    def create_shapes(self):
        # Add a centered rectangle
        self.add_shape(
            shape_type="rectangle",
            color=BOARD.BOARD_COLOR,
            width=BOARD.LENGTH,
            height=BOARD.HEIGHT,
            relative_position=(0, 0),
            centered=True
        )

        # Add a centered circle (forest ring)
        self.add_shape(
            shape_type="circle",
            color=BOARD.FOREST_COLOR,
            radius=BOARD.LENGTH/2,
            relative_position=(0, 0),
            centered=True
        )

        #Adds the colored circle arcs
        for a, c in enumerate(BOARD.SEGMENT_COLORS):
            angle_mod = (360/len(BOARD.SEGMENT_COLORS))*(a-1) #Divides the circle evenly, and enumerates by this amount

            self.add_shape(
                shape_type="arc",
                color=c,  
                radius=BOARD.LENGTH/2-BOARD.RING_DISTANCE,
                relative_position=(0, 0),  # Use (0,0) for center positioning
                angle_start=-30-angle_mod,
                angle_end=90-angle_mod,
                centered=True  # Use centered=True for center positioning
            )

        # Get the points that the hexagon will use
        hexagon_points = get_hex_points(BOARD.HEXAGON_DISTANCE)

        # Draw the hexagon and border based on the calculated points
        for i, c in enumerate([BOARD.CASTLE_COLOR, BOARD.BORDER_COLOR]):
            self.add_shape(
                shape_type="polygon",
                color=c,
                points=hexagon_points,
                centered=True,
                border_width = 6*(i) # Will either be 6 or zero
            )

        # Draw Circle outlines (the "target")
        for r in range(len(BOARD.RINGS)):
            self.add_shape(
                shape_type="circle",
                color=BOARD.BORDER_COLOR,
                radius=BOARD.LENGTH/2-(r*BOARD.RING_DISTANCE),
                centered=True,
                border_width = 5
            )

        # Angled lines, for every angle from 30 to 360 in 60 deg increments
        angled_points = get_hex_points(BOARD.LENGTH/2)

        for a in angled_points:

            self.add_shape(
                shape_type="line",
                color=BOARD.BORDER_COLOR,
                pos_start=(0, 0),
                pos_end=a,
                centered=True,
                border_width = 5
            )

        # Circles with numbers in them
        num_circle_points = get_hex_points((BOARD.LENGTH-BOARD.RING_DISTANCE)/2, 30)
        for i, c in enumerate(num_circle_points, start=1):  # Start numbering from 1
            self.add_shape(
                shape_type="circle",
                color=BOARD.BORDER_COLOR,
                radius=BOARD.RING_DISTANCE/2,
                relative_position=c,  # Adjusted midpoint relative to the center
                border_width = 2,
                centered=True  # Allows drawing relative to the center
            )

            # Add the number text
            self.add_shape(
                shape_type="text",
                color=BOARD.SEGMENT_COLORS[(((i + 3)// 2) % 3)], # Make the color of the numbers match up with the rings
                relative_position=c,  
                text=str(((i+1) % 6)+1), # Numbers from 1 to 6 in correct order
                font_size=BOARD.NUMBER_FONT_SIZE,  # Adjust font size as needed
                centered=True
            )

        # Add all the ring text labels
        for i, m in enumerate(range(-BOARD.RING_DISTANCE//2-BOARD.RING_DISTANCE, -5*BOARD.RING_DISTANCE, -BOARD.RING_DISTANCE)):
            text = BOARD.RINGS[i]
            hex_points = [x for i, x in enumerate(get_hex_points(-m)) if i % 2] # Only need half of the points
            for j, point in enumerate(hex_points):
                angle = math.degrees(math.atan2(point[1], point[0]))  # Convert (x, y) to an angle in degrees

                self.add_shape(
                    shape_type="text",
                    color= BOARD.TEXT_COLOR, 
                    relative_position=point,  
                    text=text, # "Archer, Knight, " ect...
                    font_size=BOARD.RING_FONT_SIZE,  # Adjust font size as needed
                    angle_start = -angle+270,
                    centered=True
                )

        # The middle text that says "Castl"
        self.add_shape(
            shape_type="text",
            color= BOARD.TEXT_COLOR, # Make the color of the numbers match up with the rings
            relative_position=(0,0),  
            text="Castle", # Numbers from 1 to 6 in correct order
            font_size=BOARD.RING_FONT_SIZE,  # Adjust font size as needed
            # angle_start = -angle+270,
            centered=True
        )
