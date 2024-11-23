class by_first_type(object):

    def __init__(self):
        self.__name = None

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        ??????

    def register(self, regtype):
        ??????
