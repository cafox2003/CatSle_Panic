import pygame
import math
from logic.game_logic.constants import BOARD, MONSTER, SCREEN

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

    def get_draw_function(self):
        """Returns a lambda function for drawing the shape on a screen."""
        if self.shape_type == "rectangle":
            return lambda screen: pygame.draw.rect(
                screen,
                self.color,
                (
                    BOARD.X_OFFSET + self.relative_position[0] - (self.width // 2 if self.centered else 0),  # Adjust X for centering
                    BOARD.Y_OFFSET + self.relative_position[1] - (self.height // 2 if self.centered else 0),  # Adjust Y for centering
                    self.width,  # Width of the rectangle
                    self.height  # Height of the rectangle
                ),
                self.border_width
            )
        elif self.shape_type == "circle":
            return lambda screen: pygame.draw.circle(
                screen,
                self.color,
                (
                    BOARD.X_OFFSET + self.relative_position[0],
                    BOARD.Y_OFFSET + self.relative_position[1],
                ),
                self.radius,
                self.border_width
            )
        elif self.shape_type == "polygon":
            return lambda screen: pygame.draw.polygon(
                screen,
                self.color,
                [
                    (
                        BOARD.X_OFFSET + x + self.relative_position[0],
                        BOARD.Y_OFFSET + y + self.relative_position[1],
                    )
                    for x, y in self.points
                ],
                self.border_width
            )
        elif self.shape_type == "arc":
            return lambda screen: filled_pie(
                screen,
                BOARD.X_OFFSET + self.relative_position[0],
                BOARD.Y_OFFSET + self.relative_position[1],
                self.radius,
                self.angle_start,
                self.angle_end,
                self.color
            )
        elif self.shape_type == "line":
            return lambda screen: pygame.draw.line(
                screen,
                self.color,
                (
                    BOARD.X_OFFSET + self.pos_start[0],
                    BOARD.Y_OFFSET + self.pos_start[1],
                ),
                (
                    BOARD.X_OFFSET + self.pos_end[0],
                    BOARD.Y_OFFSET + self.pos_end[1],
                ),
                self.border_width
            )
        elif self.shape_type == "text":
            return lambda screen: self._draw_text(screen)

    def _draw_text(self, screen):
        """Helper method to render text."""
        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, self.color)
        rotated_text = pygame.transform.rotate(text_surface, self.angle_start)
        rotated_rect = rotated_text.get_rect(
            center=(
                BOARD.X_OFFSET + self.relative_position[0],
                BOARD.Y_OFFSET + self.relative_position[1],
            )
        )
        screen.blit(rotated_text, rotated_rect)

def filled_pie(surface, x, y, r, start_angle, stop_angle, color):
    # Convert angles to radians
    POINTS = 100
    start_rad = math.radians(start_angle)
    stop_rad = math.radians(stop_angle)

    # Start with the center point
    points = [(x, y)]

    # Add points along the arc
    for i in range(POINTS):  
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

# Returns the angle that a point is pointed in
def get_angle(point):
    return math.degrees(math.atan2(point[1], point[0]))  
