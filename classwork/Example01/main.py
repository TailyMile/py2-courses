from time import sleep
from random import randrange
from datetime import datetime

from timing import timing

# Декорируем функцию (новый, правильный, прогрессивный способ)
@timing
def myfunc1():
    result = randrange(1,6)
    sleep(result)
    return result
    
# # Декорируем функцию. Старорежимный способ
# myfunc1 = timing(myfunc1)
    
@timing
def myfunc2(x):
    if x%2==0:
        sleep(2)
    else:
        sleep(1)
    
myfunc1()
myfunc2(myfunc1())
myfunc2(3)
