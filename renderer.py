import pygame
from gameobjects import GameObject
import typing

class Renderer:
    def __init__(self, layercount:int) -> None:
        self.screen = pygame.display.get_surface()
        self.layers = [[] for layer in range(layercount)]

    def render(self):
        self.screen.fill('blue')
        for layer in self.layers:
            object:GameObject
            for object in layer: 
                object.render()

        pygame.display.flip()

    def create_layer(self, layerlevel=None):
        if layerlevel == None:
            layerlevel = len(self.layers)    
        self.layers.append([])
    
    def add_object(self, object: GameObject, layer:int):
        self.layers[layer].append(object)

#Todo: implement layer object or maybe object group to allow derendering of large set 
#Todo: Implement culling (future thing tho)
