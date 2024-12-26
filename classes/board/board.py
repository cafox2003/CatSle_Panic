import pygame
import pygame.gfxdraw
import math
from classes.board.shape import Shape, get_hex_points, get_angle
from logic.game_logic.constants import SCREEN, BOARD

class Board:
    def __init__(self):
        self.shapes = []
        self.create_shapes()

    def add_shape(self, **kwargs):
        shape = Shape(**kwargs)
        self.shapes.append(shape.get_draw_function())

    def render(self):
        for shape in self.shapes:
            shape(SCREEN.screen)

    def create_shapes(self):
        # Add the centered square
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
                relative_position=(0, 0),
                angle_start=-30-angle_mod,
                angle_end=90-angle_mod,
                centered=True 
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

        # Draw circle outlines (the "target")
        for r in range(len(BOARD.RINGS)-1):
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
                relative_position=c,
                border_width = 2,
                centered=True
            )

            # Add the number text
            self.add_shape(
                shape_type="text",
                color=BOARD.SEGMENT_COLORS[(((i + 3)// 2) % 3)], # Make the color of the numbers match up with the rings
                relative_position=c,  
                text=str(((i+1) % 6)+1), # Numbers from 1 to 6 in correct order
                font_size=BOARD.NUMBER_FONT_SIZE,
                centered=True
            )

        # Add all the ring text labels
        for i, m in enumerate(range(-BOARD.RING_DISTANCE//2-BOARD.RING_DISTANCE, -5*BOARD.RING_DISTANCE, -BOARD.RING_DISTANCE)):
            text = BOARD.RINGS[i+1] # Skip the castle ring
            hex_points = [x for i, x in enumerate(get_hex_points(-m)) if i % 2] # Only need 3 of the points for text labels
            for j, point in enumerate(hex_points):
                angle = get_angle(point)  # Convert point to an angle

                self.add_shape(
                    shape_type="text",
                    color= BOARD.TEXT_COLOR, 
                    relative_position=point,  
                    text=text, # "Archer, Knight, " ect...
                    font_size=BOARD.RING_FONT_SIZE,  
                    angle_start = -angle+270,
                    centered=True
                )

        # The middle text that says "Castle"
        self.add_shape(
            shape_type="text",
            color= BOARD.TEXT_COLOR, 
            relative_position=(0,0),  
            text=BOARD.RINGS[0], 
            font_size=BOARD.RING_FONT_SIZE,  # Adjust font size as needed
            centered=True
        )
