import pygame
from twonk import Twonk
from renderer import Renderer
import gameobjects
Vector2 = pygame.Vector2

run = True

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

renderer = Renderer(1)
test_square = gameobjects.GameRect(Vector2(100, 100), 0, 'red', Vector2(50, 50))
twonk = Twonk()

twonk.create()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    renderer.render()


pygame.quit()