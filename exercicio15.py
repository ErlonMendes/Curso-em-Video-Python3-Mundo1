dias = int(input('Por quantos dias o carro foi alugado? '))
kmi = int(input('Qual era a quilometragem marcada na saída do carro? '))
kmf = int(input('Qual foi a quilometragem marcada na devolução do carro? '))
km = kmf - kmi
aluguel = dias*60 + km*0.15
print('O carro rodou {} km durante {} dias e o aluguel foi de R$ {:.2f}'.format(km, dias, aluguel))
