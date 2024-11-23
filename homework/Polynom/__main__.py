from polynom import Polynom

# Создаем многочлен
f = Polynom(a=2, b=3, c=1)

# Проверяем значение в точке x
x = 2
y = f(x)  # возвращаем значение многочлена в точке x
print(f"f({x}) = {y}")