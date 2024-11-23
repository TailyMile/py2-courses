import logging
logging.basicConfig(level=logging.WARNING)

from Example import Example


a = Example()

print(f'{a.color=}, {a.morning_drink=}')
a.morning_drink = 'coffee'
print(f'{a.color=}, {a.morning_drink=}')
a.color = 'blue'
print(f'{a.color=}, {a.morning_drink=}')
