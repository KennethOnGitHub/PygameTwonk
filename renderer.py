import pygame
import gameobjects

class Renderer:
    def __init__(self) -> None:
        self.screen = pygame.display.get_surface()

    def render(self, gameobjects:list):
        for gameobject in gameobjects:
            
