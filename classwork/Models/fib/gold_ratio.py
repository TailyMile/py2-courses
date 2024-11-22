from Fibonacci import Fibonacci
from fractions import Fraction


# функция-генератор
def gold_ratio(eps=None):
    fib = iter(Fibonacci(1,1))
    a = next(fib)
    prev = None
    for b in fib:
        result = Fraction(b,a)
        a = b
        yield result
        # отсюда продолжается выполнение
        # при запросе следующего элемента
        if prev is not None:
            delta = abs(prev-result)
            if delta < eps:
                break
        prev = result
            
        
    