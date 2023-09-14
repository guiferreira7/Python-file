ax = float(input('Qual o valor de ax:'))
bx = float(input('Qual o valor de bx:'))
c = float(input('Qual o valor de c:'))
delta = (bx ** 2) - 4 * ax * c
x1 = (-bx + delta ** (1 / 2)) / (2 * ax)
x2 = (-bx - delta ** (1 / 2)) / (2 * ax)
print("x1: {}, x2: {}".format(x1, x2))
