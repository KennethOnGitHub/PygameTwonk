# import pygame
# from twonk import Twonk
# from renderer import Renderer
# import gameobjects
# Vector2 = pygame.Vector2

# run = True

# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()

# renderer = Renderer(1)
# test_square = gameobjects.GameRect(Vector2(100, 100), 0, 'red', Vector2(50, 50))
# twonk = Twonk()

# twonk.create()

# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     renderer.render()


# pygame.quit()

import pygame


import twonk

twonk.innit_bruv(screensize=pygame.Vector2(1366, 768), layercount=1, backgroundcolour='blue')

testsqure = twonk.gameobjects.GameRect(pygame.Vector2(50, 50), 0, 'red', pygame.Vector2(50, 50))
testline = twonk.gameobjects.GameLine(pygame.Vector2(200, 200), 0, 'black', pygame.Vector2(500, 500), 3)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    twonk.update()