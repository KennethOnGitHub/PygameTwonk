import pygame
import gameobjects
import renderer

objects = []

def add_object(object):
    objects.append(object)
    renderer.add_object(object)

def update_objects():
    object:gameobjects.GameObject
    for object in objects:
        object.update()

        