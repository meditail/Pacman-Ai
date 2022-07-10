import pygame

pygame.init()

FPS = 30
WINDOW_SIZE = (WIDTH, HEIGHT) = 800, 400
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
