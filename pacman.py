import pygame
import enum
from color import Color

RADIUS = 25
SPEED = 5


class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None

    def switch_direction(self, new_direction):
        self.direction = new_direction

    def move(self):
        if self.direction == Direction.up:
            self.y -= SPEED
        elif self.direction == Direction.down:
            self.y += SPEED
        elif self.direction == Direction.left:
            self.x -= SPEED
        elif self.direction == Direction.right:
            self.x += SPEED

    def draw(self, window):
        pygame.draw.circle(window, Color.yellow, (self.x, self.y), RADIUS)


class Direction(enum.Enum):
    up = 1
    down = 2
    right = 3
    left = 4




