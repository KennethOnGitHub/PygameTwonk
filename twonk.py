import pygame
import gameobjects
from renderer import Renderer
Vector2 = pygame.Vector2

class Twonk:
    def __init__(self) -> None:
        self.renderer:Renderer = Renderer()
        self.gameobjects = gameobjects

    def create_screen(self, screensize:Vector2) -> None:
        pass