from LogContext import LogContext, InterruptContext

import logging
logging.basicConfig(level=logging.DEBUG)

def fun(a, b):
    with LogContext('Internal 1') as name:
        print(a*b)
        print(a+b)
        if a < b:
            return
        print(a/b)


with LogContext('First') as ctx_name:
    print('Ура!!!')
    print(ctx_name)

print(40*'-')
fun(6,5)
print(40*'-')
fun(5,6)
print(40*'-')
# fun(5,0)

print(40*'-')

with LogContext('Вася'):
    name = input('Как тебя зовут?: ')
    age = int(input('Сколько тебе лет?: '))
    if age < 6:
        raise InterruptContext()
    print(f'Тебе, {name} завтра пора в школу')
