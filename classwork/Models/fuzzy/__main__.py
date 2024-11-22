p = Zone(56, 98)
q = Zone(101, 78)
s = Zone(150, 200)

w = p + q
z = p + s  # Исключение

p += q
p += s # Исключение


reg = Region(10, 100)
reg.append(p)
reg.append(z)

uncovered = ~reg