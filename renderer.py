import pygame
from gameobjects import GameObject
import typing

class Renderer:
    def __init__(self, layercount:int) -> None:
        self.screen = pygame.display.get_surface()
        self.layers = [[] for layer in range(layercount)]

    def render(self):
        for layer in self.layers:
            object:GameObject
            for object in layer: 
                object.render()

    def create_layer(self, layerlevel=None):
        if layerlevel == None:
            layerlevel = len(self.layers)    
        self.layers.append([])

#Todo: implement layer object or maybe object group to allow derendering of large set
#Todo: Implement culling (future thing tho)
