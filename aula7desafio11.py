larg = float(input('Digite a largura da parede (m) '))
alt = float(input('Digite a altura da parede (m) '))
area = larg*alt
v = area/2
print('Sua parede tem {:.2f} m² e precisará de {:.2f} L de tinta para pintá-la.'.format(area, v))
