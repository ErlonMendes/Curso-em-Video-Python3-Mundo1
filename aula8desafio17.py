from math import sqrt, pow, hypot
catop = float(input('Digite o comprimento do cateto 1: '))
catadj = float(input('Digite o comprimento do cateto 2: '))
hip = (catop**2 + catadj**2)**(1/2)
print('A hipotenusa do triângulo retângulo de catetos {} e {} é {:.3f}'.format(catop, catadj, hip))
hip2 = sqrt(pow(catop, 2)+pow(catadj, 2))
print('A hipotenusa do triângulo retângulo de catetos {} e {} é {:.3f}'.format(catop, catadj, hip2))
# Usando hypot, fica
hip3 = hypot(catop, catadj)
print('A hipotenusa do triângulo retângulo de catetos {} e {} é {:.3f}'.format(catop, catadj, hip3))
