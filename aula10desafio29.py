v = int(input('Escreva a velocidade do carro (km/h): '))
if v > 80:
    multa = (v - 80)*7
    print('\033[1;31mVocê excedeu o limite de velocidade de 80 km/h e foi multado em R$ {:.2f}\033[m'.format(multa))
else:
    print('\033[1;32m{} km/h\033[m'.format(v))
