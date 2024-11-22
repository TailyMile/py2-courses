from BCoords import BCoords

crd = BCoords( (1,1), (1,2), (2,1) )

p = crd(1, 1, 2)
print(p)

p = crd(3, 1, -2)
print(p)

