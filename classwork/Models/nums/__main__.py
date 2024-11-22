from Vector3d import Vector3d

a = Vector3d(1, 2, 1)
b = Vector3d(2, 2, 2)

print('a =', a)
print('b =', b)
print('a+b =', a+b)
print('b+a =', b+a)

print(f'{a*5=}')
print(f'{b*10=}')

print(f'{3*a=}')
print(f'{5*b=}')

q = abs(a)
print(f'{q=}')

a += b
print(f'{a=}')
b *= 3
print(f'{b=}')
