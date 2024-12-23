import pygame
import math

class Shape:
    def __init__(self, shape_type, color, relative_position=(0, 0), border_width=0, width=0, height=0, radius=0, 
                 angle_start=0, angle_end=0, pos_start=(0,0), pos_end=(0,0), points=[], text="", font_size=0, centered=False):
        self.shape_type = shape_type
        self.color = color
        self.relative_position = relative_position
        self.border_width = border_width
        self.width = width
        self.height = height
        self.radius = radius
        self.angle_start = angle_start
        self.angle_end = angle_end
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.points = points
        self.text = text
        self.font_size = font_size
        self.centered = centered

    def get_draw_function(self, board_length, board_height):
        """Returns a lambda function for drawing the shape on a screen."""
        if self.shape_type == "rectangle":
            return self._get_rectangle_draw_function(board_length, board_height)
        elif self.shape_type == "circle":
            return self._get_circle_draw_function(board_length, board_height)
        elif self.shape_type == "arc":
            return self._get_arc_draw_function(board_length, board_height)
        elif self.shape_type == "line":
            return self._get_line_draw_function(board_length, board_height)
        elif self.shape_type == "polygon":
            return self._get_polygon_draw_function(board_length, board_height)
        elif self.shape_type == "text":
            return self._get_text_draw_function(board_length, board_height)
        else:
            raise ValueError(f"Unsupported shape type: {self.shape_type}")

    def _get_rectangle_draw_function(self, board_length, board_height):
        return lambda screen, x_offset, y_offset: pygame.draw.rect(
            screen,
            self.color,
            (
                (x_offset if self.centered else self.relative_position[0]),  # X-coordinate
                (y_offset if self.centered else self.relative_position[1]),  # Y-coordinate
                self.width,  # Width of the rectangle
                self.height  # Height of the rectangle
            ),
            self.border_width
        )

    # def _get_circle_draw_function(self, board_length, board_height):
    #     return lambda screen, x_offset, y_offset: pygame.draw.circle(
    #         screen,
    #         self.color,
    #         (
    #             (x_offset if self.centered else self.relative_position[0]) + board_length // 2,  # Adjust X-coordinate for circle center
    #             (y_offset if self.centered else self.relative_position[1]) + board_height // 2  # Adjust Y-coordinate for circle center
    #         ),
    #         # (
    #         #     (x_offset if self.centered else self.relative_position[0]) + board_length // 2,  # Adjust X-coordinate for circle center
    #         #     (y_offset if self.centered else self.relative_position[1]) + board_height // 2  # Adjust Y-coordinate for circle center
    #         # ),
    #         self.radius,  # Radius of the circle
    #         self.border_width
    #     )

    def _get_circle_draw_function(self, board_length, board_height):
        return lambda screen, x_offset, y_offset: pygame.draw.circle(
            screen,
            self.color,
            (
                (self.relative_position[0] if not self.centered else board_length // 2) + x_offset + self.relative_position[0],
                (self.relative_position[1] if not self.centered else board_height // 2) + y_offset + self.relative_position[1],
            ),
            self.radius,  # Radius of the circle
            self.border_width
        )

    
    def _get_polygon_draw_function(self, board_length, board_height):
        return lambda screen, x_offset, y_offset: pygame.draw.polygon(
                screen,
                self.color,
                [
                    (
                        board_length/2 + x + (x_offset if self.centered else self.relative_position[0]),
                        board_height/2 + y + (y_offset if self.centered else self.relative_position[1])
                        )
                    for x, y in self.points  # Adjust points based on offsets and centering
                    ],
                self.border_width
                ) 

    def _get_arc_draw_function(self, board_length, board_height):
        return lambda screen, x_offset, y_offset: filled_pie(
            screen,
            (x_offset if self.centered else self.relative_position[0]) + board_length // 2,  # x center
            (y_offset if self.centered else self.relative_position[1]) + board_height // 2,  # y center
            self.radius,  # radius
            self.angle_start,  # start angle
            self.angle_end,  # end angle
            self.color  # color
        )


    def _get_line_draw_function(self, board_length, board_height):
        return lambda screen, x_offset, y_offset: pygame.draw.line(
            screen,
            self.color,
            (
                (self.relative_position[0] if not self.centered else board_length // 2) + self.pos_start[0] + x_offset,
                (self.relative_position[1] if not self.centered else board_height // 2) + self.pos_start[1] + y_offset,
            ),
            (
                (self.relative_position[0] if not self.centered else board_length // 2) + self.pos_end[0] + x_offset,
                (self.relative_position[1] if not self.centered else board_height // 2) + self.pos_end[1] + y_offset,
            ),
            self.border_width
        )
    def _get_text_draw_function(self, board_length, board_height):
        def draw_text(screen, x_offset, y_offset):
            # Create a font object and render the text
            font = pygame.font.Font(None, self.font_size)  # Default font with specified size
            text_surface = font.render(self.text, True, self.color)

            # Rotate the text surface
            rotated_text = pygame.transform.rotate(text_surface, self.angle_start)  # Use angle_start or another angle if needed

            # Get the new rect after rotation, so we can center it correctly
            rotated_rect = rotated_text.get_rect(
                center=(
                    (self.relative_position[0] if not self.centered else board_length // 2) + x_offset + self.relative_position[0],
                    (self.relative_position[1] if not self.centered else board_height // 2) + y_offset + self.relative_position[1]
                )
            )

            # Blit the rotated text
            screen.blit(rotated_text, rotated_rect)
        
        return draw_text

def filled_pie(surface, x, y, r, start_angle, stop_angle, color):
    # Convert angles to radians
    POINTS = 30

    start_rad = math.radians(start_angle)
    stop_rad = math.radians(stop_angle)

    # Start with the center point
    points = [(x, y)]

    # Add points along the arc (12 segments should be smooth enough)
    for i in range(POINTS):  # 13 points = 12 segments
        angle = start_rad + (stop_rad - start_rad) * (i / (POINTS-1))
        points.append((
            x + r * math.cos(angle),
            y - r * math.sin(angle)  # Subtract because pygame Y coordinates go down
            ))

    # Draw the filled polygon
    return pygame.draw.polygon(surface, color, points)

# Return points along the guiding lines, or in relation to them
def get_hex_points(magnitude, angle_mod=0):
    points = []
    for a in range(30, 361, 60):
        angled_point = (magnitude * math.cos(math.radians(a+angle_mod)), magnitude * math.sin(math.radians(a+angle_mod)))
        points.append(angled_point)

    return points
