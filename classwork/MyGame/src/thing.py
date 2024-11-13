from abc import abstractmethod

class Thing (object):

    @abstractmethod
    def move(self, delta_t):
        pass

    @abstractmethod
    def draw(self, window):
        pass