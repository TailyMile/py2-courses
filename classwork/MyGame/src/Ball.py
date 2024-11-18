import pygame
from Thing import Thing
from Stage import Stage


class Ball(Thing):

    def __init__(self, pos, vel, radius, color, mass=1.0):
        super().__init__(pos)
        self.__vx = vel[0]
        self.__vy = vel[1]
        self.__radius = radius
        self.__color = color
        self.__mass = mass
        
    @property
    def vel(self):
        return (self.__vx, self.__vy)
        
    def draw(self, window):
        pygame.draw.circle(window, self.__color, self.pos, self.__radius)
        
    def bang(self, other=None):
    
        if other is None:
            # Столкновение с элементом Вселенной (граница окна)
            width, height = Stage.inst().window_size
            x, y = self.pos
            if x < self.__radius and self.__vx < 0:
                self.__vx = -self.__vx
            elif x > width - self.__radius and self.__vx > 0:
                self.__vx = -self.__vx
            elif y < self.__radius and self.__vy < 0:
                self.__vy = - self.__vy
            elif y > height - self.__radius and self.__vy > 0:
                self.__vy = - self.__vy

        else:
            # Столкновение шарика с другим объектом
            pass
        
