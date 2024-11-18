from random import randrange, gauss
from Stage import Stage
from Ball import Ball


class MyStage(Stage):

    def setup(self):
        super().setup()
        w, h = self.window_size
        for k in range(0,10):
            x = randrange(0, w)
            y = randrange(0, h)
            vx = gauss(0, 50)
            vy = gauss(0, 50)
            b = Ball(pos=(x,y), vel=(vx,vy), color=(255,0,0), radius=10)
            self.add_thing(b)
        for k in range(0,10):
            x = randrange(0, w)
            y = randrange(0, h)
            vx = gauss(0, 50)
            vy = gauss(0, 50)
            b = Ball(pos=(x,y), vel=(vx,vy), color=(248,255,0), radius=5, mass=0.1)
            self.add_thing(b)
