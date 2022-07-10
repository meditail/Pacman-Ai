import pygame
from color import Color
from pacman import Pacman, Direction

pygame.init()

FPS = 30
WINDOW_SIZE = (WIDTH, HEIGHT) = 800, 400
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

pacman = Pacman(100, 100)
running = True
clock = pygame.time.Clock()

pacman.switch_direction(Direction.down)


def draw_all():
    WINDOW.fill(Color.black)
    pacman.draw(WINDOW)


def move_all():
    pacman.move()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_all()
    draw_all()

    pygame.display.update()
    clock.tick(FPS)
