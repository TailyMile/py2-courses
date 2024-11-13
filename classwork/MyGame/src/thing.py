from abc import abstractmethod, ABCMeta

class Thing (object, metaclass=ABCMeta):

    def __init__(self, pos):
        self.__x = pos[0]
        self.__y = pos[1]

    @property
    def pos(self):
        return(self.__x, self.__y)

    @abstractmethod
    def move(self, delta_t):
        vx, vy = self.vel
        self.__x += vx * delta_t
        self.__y += vy * delta_t
    
    @property
    def vel(self):
        return(0,0)

    @abstractmethod
    def draw(self, window):
        pass