import pygame
from color import Color
from pacman import Pacman, Direction

pygame.init()

FPS = 30
WINDOW_SIZE = (WIDTH, HEIGHT) = 800, 400
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
BRICK_SIZE = 50

pacman = Pacman(100, 100)
running = True
clock = pygame.time.Clock()

# 0 wall, 1 path, 2 coins, 3 pacman, 4 bad_guy
LEVEL = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
rows = 8
cols = 16


def draw_level():
    for row in range(rows):
        for col in range(cols):
            if LEVEL[row * cols + col] == 0:
                pygame.draw.rect(WINDOW, Color.blue, (col * BRICK_SIZE, row * BRICK_SIZE, BRICK_SIZE, BRICK_SIZE))


def draw_all():
    WINDOW.fill(Color.black)
    draw_level()
    pacman.draw(WINDOW)


def move_all():
    pacman.move()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pacman.switch_direction(Direction.up)
            if event.key == pygame.K_s:
                pacman.switch_direction(Direction.down)
            if event.key == pygame.K_d:
                pacman.switch_direction(Direction.right)
            if event.key == pygame.K_a:
                pacman.switch_direction(Direction.left)

    move_all()
    draw_all()

    pygame.display.update()
    clock.tick(FPS)
