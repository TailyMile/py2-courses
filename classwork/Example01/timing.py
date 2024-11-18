from datetime import datetime


# Функция-декоратор
def timing(function):
    def timed_function(*args, **kwargs):
        t0 = datetime.now()
        result = function(*args, **kwargs)
        t1 = datetime.now()
        d = ( t1 - t0 ).total_seconds()
        print(function.__name__, ':', d)
        return result
    return timed_function
