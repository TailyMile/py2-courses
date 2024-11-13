import pygame
import exceptions as exc


class Stage(object):

    __inst = None

    @classmethod
    def inst(cls):
        return cls.__inst

    def __init__(self, window_size=(1024,768)):
        self.__window_size = window_size
        self.__background = ( 0, 0, 0 )
        self.__window = None
        self.__contents = []
        self.__time = None
        Stage.__inst = self

    @property
    def window_size(self):
        return self.__window_size
       
    @window_size.setter
    def window_size(self, value):
        if self.__window is None:
            self.__window_size = value
        else:
            raise exc.InvalidOperation('Cannot change size of active window')
        
    @property
    def background(self):
        return self.__background
    
    def clear(self):
        self.__window.fill(self.background)

    def flip(self):
        pygame.display.update()

    def update(self):
        t = pygame.time.get_ticks() / 1000.0
        delta_t = t - self.__time
        self.__time = t
        for x in self.__contents:
            x.move(delta_t)

    def draw(self):
        for x in self.__contents:
            x.draw(self.__window)

    def setup(self):
        pass

    def add_thing(self, x):
        self.__contents.append(x)

    def dispatch(self):
        events = pygame.event.get()
        for ev in events:
            if ev.type == pygame.QUIT:
                raise exc.GameOver()
        
    def main_loop(self):
        pygame.init()

        self.setup()

        try:
            self.__window = pygame.display.set_mode(self.window_size)
            self.__time = pygame.time.get_ticks() / 10000.0
            try:
                while True:
                    # 1. Events exception
                    self.dispatch()

                    # 2. update
                    self.update()

                    # 3. clear
                    self.clear()

                    # 4. render
                    self.draw()

                    # 5. flip
                    self.flip()
                    
            except exc.GameOver:
                pass
                
        finally:
            pygame.quit()
            self.__window = None