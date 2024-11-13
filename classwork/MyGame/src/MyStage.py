from Stage import Stage
from ball import Ball

class MyStage(Stage):

    def setup(self):
        super().setup()
        b = Ball(pos=(100,100), vel=(20,15), color=(255,0,0), radius=10)
        self.add_thing(b)
