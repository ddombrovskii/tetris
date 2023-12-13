import pygame

# just testing some shitpost

BACKGROUND_COLOR = (234, 212, 252)

screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('Tetris')

screen.fill(BACKGROUND_COLOR)

pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
