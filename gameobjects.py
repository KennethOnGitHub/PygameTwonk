import pygame
import objecthandler
from abc import ABC, abstractmethod

Vector2 = pygame.Vector2

class GameObject(ABC):
    def __init__(self, position:Vector2, layer:int) -> None:
        self.surface = pygame.display.get_surface() # may change this in the future
        self.position:pygame.Vector2 = position
        self.layer:int = layer
        objecthandler.add_object(self)

    def update(self):
        pass

    def render(self):
        pass

    def moveto(self, new_pos:Vector2):
        self.position = new_pos

    def moveby(self, move_vector:Vector2):
        self.position += move_vector
    
    def get_pos(self):
        return self.position

    def resizeto(self):
        pass

    def resizeby(self):
        pass


class GameLine(GameObject):
    def __init__(self, position:Vector2, layer: int, colour:pygame.Color, endpos: Vector2, width:int) -> None:
        super().__init__(position, layer)
        self.colour = colour
        self.startpos:Vector2 = position #not sure if its a good idea to have position AND startpos tbh, but oh well! :D
        self.endpos:Vector2 = endpos
        self.width:int = width
    
    def render(self):
        pygame.draw.line(self.surface, self.colour, self.startpos, self.endpos, self.width)

class GameRect(GameObject):
    def __init__(self, position: Vector2, layer: int, colour:pygame.Color, size:Vector2) -> None:
        super().__init__(position, layer)
        self.colour = colour
        self.size = size
    
    def render(self):
        self.rect = pygame.Rect(self.position - self.size/2, self.size) #creating rects every frame may be a little bad for performance, but I think it will reduce the number of bugs in the future
        pygame.draw.rect(self.surface, self.colour, self.rect) #issue, moving squares will not update the rect

        

class Sprite(GameObject):
    def __init__(self, position: Vector2, layer: int) -> None:
        super().__init__(position, layer)
        
