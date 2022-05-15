dias = int(input('Por quantos dias o carro foi alugado? '))
kmi = float(input('Qual era a quilometragem marcada na saída do carro? '))
kmf = float(input('Qual foi a quilometragem marcada na devolução do carro? '))
km = kmf - kmi
aluguel = dias*60 + km*0.15
print('O carro rodou {:.1f} km durante {} dias e o aluguel foi de R$ {:.2f}'.format(km, dias, aluguel))
