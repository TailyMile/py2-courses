class OperationNotPermitted(Exception):
    pass


class Zone(object):

    def __init__(self, a:float, b:float):
        self.__a, self.__b = sorted([a,b])

    def __add__(self, other):
        if self.__b < other.__a or other.__b < self.__a:
            raise OperationNotPermitted()
        a = min(self.__a, other.__a)
        b = max(self.__b, other.__b)
        return Zone(a, b)

    def __contains__(self, other) -> bool:
        return self.__a <= other.__a and self.__b >= other.__b
