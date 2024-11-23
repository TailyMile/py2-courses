import logging
logging.basicConfig(level=logging.WARNING)

from example import Example

a = Example(10)

# Проверяем значение
print(f'{a.value=}')

a.value = 5
print(f'{a.value=}')

# Пробуем установить отрицательное значение
try:
    a.value = -3
except ValueError as e:
    print(f"Ошибка: {e}") 