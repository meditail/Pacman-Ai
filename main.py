import pygame
from color import Color
from pacman import Pacman, Direction

pygame.init()

FPS = 30
WINDOW_SIZE = (WIDTH, HEIGHT) = 800, 400
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
BRICK_SIZE = 50

pacman = Pacman(100, 100)
next_direction = None
running = True
clock = pygame.time.Clock()

# 0 wall, 1 path, 2 coins, 3 pacman, 4 bad_guy, 5 power_up
LEVEL = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
rows = 8
cols = 16


def draw_level():
    for row in range(rows):
        for col in range(cols):
            if LEVEL[row * cols + col] == 0:  # wall
                pygame.draw.rect(WINDOW, Color.blue, (col * BRICK_SIZE, row * BRICK_SIZE, BRICK_SIZE, BRICK_SIZE))
            elif LEVEL[row * cols + col] == 2:  # coins
                pygame.draw.circle(WINDOW, Color.yellow, (col * BRICK_SIZE + 25, row * BRICK_SIZE + 25), 5)
            elif LEVEL[row * cols + col] == 3:
                pacman.x = col * BRICK_SIZE + 25
                pacman.y = row * BRICK_SIZE + 25
                LEVEL[row * cols + col] = 1


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
                next_direction = Direction.up
            if event.key == pygame.K_s:
                next_direction = Direction.down
            if event.key == pygame.K_d:
                next_direction = Direction.right
            if event.key == pygame.K_a:
                next_direction = Direction.left

    move_all()
    draw_all()

    pacman_pos_on_level_row = (pacman.y - 25) / BRICK_SIZE
    pacman_pos_on_level_col = (pacman.x - 25) / BRICK_SIZE

    can_move_up = False
    can_move_down = False
    can_move_right = False
    can_move_left = False

    if pacman_pos_on_level_row.is_integer() and pacman_pos_on_level_col.is_integer():
        pacman_pos_on_level = int(pacman_pos_on_level_row * cols + pacman_pos_on_level_col)
        print(LEVEL[pacman_pos_on_level - 16])
        can_move_up = LEVEL[pacman_pos_on_level - 16] == 1
        can_move_down = LEVEL[pacman_pos_on_level + 16] == 1
        can_move_right = LEVEL[pacman_pos_on_level + 1] == 1
        can_move_left = LEVEL[pacman_pos_on_level - 1] == 1

    if next_direction == Direction.up and can_move_up:
        pacman.switch_direction(Direction.up)
    elif next_direction == Direction.down and can_move_down:
        pacman.switch_direction(Direction.down)
    elif next_direction == Direction.right and can_move_right:
        pacman.switch_direction(Direction.right)
    elif next_direction == Direction.left and can_move_left:
        pacman.switch_direction(Direction.left)

    pygame.display.update()
    clock.tick(FPS)
