import pygame
from gameobjects import GameObject

layers:list
background_colour:pygame.color

#todo, make a twonk settings that will make twonk defaults, but not for me to crack open in the future(maybe)
def init(layercount:int=1, colour:pygame.color='blueviolet'):
    global layers #fix this later, the globals might be a little bad, idk
    global background_colour
    global screen
    layers = [[] for x in range(layercount)]
    background_colour = colour
    screen = pygame.display.get_surface()

def render():
    screen.fill(background_colour)
    for layer in layers:
        object:GameObject
        for object in layer: 
            object.render()

    pygame.display.flip()

def add_layer( layerlevel=None):
    if layerlevel == None:
        layerlevel = len(layers)    
    layers.append([])

def add_object(object: GameObject):
    layers[object.layer].append(object)

#Todo: implement layer object or maybe object group to allow derendering of large set 
#Todo: Implement culling (future thing tho)
