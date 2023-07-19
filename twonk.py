import pygame

import objecthandler
import gameobjects
import renderer

def innit_bruv(screensize:pygame.Vector2, layercount:int, backgroundcolour:pygame.color):
    pygame.display.set_mode(screensize)

    renderer.init(layercount, backgroundcolour)

def update():
    objecthandler.update_objects()
    renderer.render()


