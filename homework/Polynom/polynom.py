class Polynom(object):
    def __init__(self, a=0, b=0, c=0):
        self.__a = a  # Коэффициент при x^0
        self.__b = b  # Коэффициент при x^1
        self.__c = c  # Коэффициент при x^2

    def __call__(self, x):
        # Явно вычисляем многочлен степени не выше второй
        result = self.__a + self.__b * x + self.__c * (x ** 2)
        return result