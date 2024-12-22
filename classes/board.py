import pygame
import pygame.gfxdraw
import math
from classes.shape import Shape
class Board:
    def __init__(self, length=900, height=900):
        self.RING_DISTANCE = 95
        self.HEXAGON_DISTANCE = self.RING_DISTANCE * 1.25
        self.COLORS = [(255,0,0),(0,255,0),(0,0,255)]


        self.length = length
        self.height = height
        self.shapes = []

        self.create_shapes()

    def add_shape(self, shape_type, color, relative_position=(0, 0), border_width=0, width=0, height=0, radius=0, 
                 angle_start=0, angle_end=0, pos_start=(0,0), pos_end=(0,0), points=[], text="", font_size=0, centered=False):
        shape = Shape(shape_type, color, relative_position, border_width, width, height, radius, angle_start, angle_end,
                      pos_start, pos_end, points, text, font_size, centered)

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
        self.add_shape(
            shape_type="circle",
            color=(63, 117, 57),
            radius=500,
            relative_position=(0, 0),
            centered=True
        )

        #Adds the colored circle arcs
        for a, c in enumerate(self.COLORS):
            angle_mod = (360/len(self.COLORS))*(a-1) #Divides the circle evenly, and enumerates by this amount

            self.add_shape(
                shape_type="arc",
                color=c,  # Blue
                radius=self.length/2-self.RING_DISTANCE,
                relative_position=(0, 0),  # Use (0,0) for center positioning
                angle_start=-30-angle_mod,
                angle_end=90-angle_mod,
                centered=True  # Use centered=True for center positioning
            )



        # Get the points that the hexagon will use
        hexagon_points = []
        for a in range(30, 361, 60):
            # Add the inner hexagon
            current_node = (self.HEXAGON_DISTANCE * math.cos(math.radians(a)), self.HEXAGON_DISTANCE * math.sin(math.radians(a)))

            hexagon_points.append(current_node)


        # Draw the hexagon and border based on the calculated points
        for i, c in enumerate([(100,100,100), (0, 0, 0)]):
            self.add_shape(
                shape_type="polygon",
                color=c,
                points=hexagon_points,
                centered=True,
                border_width = 6*(i) # Will either be 6 or zero
            )


        # Draw Circle outlines (the "target")
        for r in range(4):
            self.add_shape(
                shape_type="circle",
                color=(0, 0, 0),
                radius=self.length/2-(r*self.RING_DISTANCE),
                centered=True,
                border_width = 5
            )

        num_circle_points = []
        # Angled lines, for every angle from 30 to 360 in 60 deg increments
        for a in range(30, 361, 60):
            # Add the "disecting" lines
            angled_point = (self.length/2 * math.cos(math.radians(a)), self.length/2 * math.sin(math.radians(a)))

            # 60/2 = 30, so the midpoints will be 30 degrees above. Adds the midpoints for the circles with numbers
            num_circle_point = ((self.length-self.RING_DISTANCE)/2 * math.cos(math.radians(a+30)),
                                (self.length-self.RING_DISTANCE)/2 * math.sin(math.radians(a+30)))

            num_circle_points.append(num_circle_point)

            self.add_shape(
                shape_type="line",
                color=(0, 0, 0),
                pos_start=(0, 0),
                pos_end=angled_point,
                centered=True,
                border_width = 5
            )

        for i, c in enumerate(num_circle_points, start=1):  # Start numbering from 1
            self.add_shape(
                shape_type="circle",
                color=(0, 0, 0),
                radius=self.RING_DISTANCE/2,
                relative_position=c,  # Adjusted midpoint relative to the center
                border_width = 2,
                centered=True  # Allows drawing relative to the center
            )

            # Add the number text
            self.add_shape(
                shape_type="text",
                color=self.COLORS[(((i + 3)// 2) % 3)], 
                relative_position=c,  # Same position as the circle
                text=str(((i+1) % 6)+1), # Numbers from 1 to 6 in correct order
                # text=str(i % 6 + 1),
                font_size=90,  # Adjust font size as needed
                centered=True
            )
