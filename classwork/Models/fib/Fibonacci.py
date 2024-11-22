class FibonacciIterator(object):
    '''
        Итератор
    '''
    
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __next__(self):
        result = self.__a
        self.__a = self.__b
        self.__b = self.__b + result
        return result
        
    def __iter__(self):
        return self


class Fibonacci(object):
    '''
        Генератор
    '''

    def __init__(self, a=1, b=1):
        self.__a = a
        self.__b = b
        
    def __iter__(self):
        it = FibonacciIterator(self.__a, self.__b)
        return it
        
    def __str__(self):
        return f'Fibonacci({self.__a}, {self.__b})'
        
    def __repr__(self):
        return self.__str__()
