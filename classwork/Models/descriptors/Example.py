from OneOf import OneOf


class Example(object):

    color = OneOf('red', 'green', 'blue')
    morning_drink = OneOf('tea', 'coffee', 'brandy', 'bear')

    def __init__(self):
        pass