import pygame
import pygame.gfxdraw
import math
from classes.shape import Shape
class Board:
    def __init__(self, length=900, height=900):
        self.RING_DISTANCE = 100

        self.length = length
        self.height = height
        self.shapes = []

        self.create_shapes()

    def add_shape(self, shape_type, color, relative_position=(0, 0), border_width=0, width=0, height=0, radius=0, 
                 angle_start=0, angle_end=0, pos_start=(0,0), pos_end=(0,0), points=[], centered=False):
        shape = Shape(shape_type, color, relative_position, border_width, width, height, radius, angle_start, angle_end,
                      pos_start, pos_end, points, centered)

        draw_function = shape.get_draw_function(self.length, self.height)
        self.shapes.append(draw_function)

    def create_shapes(self):
        # Add a centered rectangle
        self.add_shape(
            shape_type="rectangle",
            color=(63, 117, 57),
            width=self.length,
            height=self.height,
            relative_position=(0, 0),
            centered=True
        )

        # Add a centered circle
        # self.add_shape(
        #     shape_type="circle",
        #     color=(63, 117, 57),
        #     radius=450,
        #     relative_position=(500, 500),
        #     centered=True
        # )

        #Adds the circle arcs
        colors = [(255,0,0),(0,255,0),(0,0,255)]
        for a, c in enumerate(colors):
            angle_mod = (360/len(colors))*(a-1) #Divides the circle evenly, and enumerates by this amount

            self.add_shape(
                shape_type="arc",
                color=c,  # Blue
                radius=self.length/2-self.RING_DISTANCE,
                relative_position=(0, 0),  # Use (0,0) for center positioning
                angle_start=-30+angle_mod,
                angle_end=90+angle_mod,
                centered=True  # Use centered=True for center positioning
            )


        # Get the points that the hexagon will use
        SMALL_LINE_DIST = 125
        hexagon_points = []
        for a in range(30, 361, 60):
            # Add the inner hexagon
            current_node = (SMALL_LINE_DIST * math.cos(math.radians(a)), SMALL_LINE_DIST * math.sin(math.radians(a)))

            hexagon_points.append(current_node)


        # Draw the hexagon and border
        for i, c in enumerate([(100,100,100), (0, 0, 0)]):
            self.add_shape(
                shape_type="polygon",
                color=c,
                points=hexagon_points,
                centered=True,
                border_width = 6*(i) # Will either be 6 or zero
            )


        # Draw Circle outlines
        for r in range(4):
            self.add_shape(
                shape_type="circle",
                color=(0, 0, 0),
                radius=self.length/2-(r*self.RING_DISTANCE),
                centered=True,
                border_width = 5
            )

        # Angled lines, for every angle from 30 to 360 in 60 deg increments
        for a in range(30, 361, 60):
            # Add the "disecting" lines
            self.add_shape(
                shape_type="line",
                color=(0, 0, 0),
                pos_start=(0, 0),
                pos_end=(self.length/2 * math.cos(math.radians(a)), self.length/2 * math.sin(math.radians(a))),
                centered=True,
                border_width = 5
            )


