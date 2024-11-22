class BCoords(object):

    def __init__(self, point_a, point_b, point_c):
        self.__a_x, self.__a_y = point_a
        self.__b_x, self.__b_y = point_b
        self.__c_x, self.__c_y = point_c

    def __call__(self, ma, mb, mc):
        x = ( ma*self.__a_x + mb*self.__b_x + mc*self.__c_x) / (ma+mb+mc)
        y = ( ma*self.__a_y + mb*self.__b_y + mc*self.__c_y) / (ma+mb+mc)
        return (x, y)
