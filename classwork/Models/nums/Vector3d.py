from math import sqrt


class InvalidOperation(Exception):
    pass


class Vector3d(object):

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return f'<{self.__x} {self.__y} {self.__z}>'

    __repr__ = __str__

    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y
        z = self.__z + other.__z
        return Vector3d(x, y, z)

    def __mul__(self, number):
        x = self.__x * number
        y = self.__y * number
        z = self.__z * number
        return Vector3d(x, y, z)

    __rmul__ = __mul__

    def __abs__(self):
        return sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def __iadd__(self, other):
        self.__x += other.__x
        self.__y += other.__y
        self.__z += other.__z
        return self

    def __imul__(self, other):
        raise InvalidOperation()
