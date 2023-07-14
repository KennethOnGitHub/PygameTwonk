import pygame
run = True

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pos = pygame.Vector2(400, 400)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    testRect = pygame.Rect(pos, pos)
    pygame.draw.rect(screen, "red", testRect)
    pygame.display.flip()

pygame.quit()