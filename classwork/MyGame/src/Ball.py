import pygame
from thing import Thing

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