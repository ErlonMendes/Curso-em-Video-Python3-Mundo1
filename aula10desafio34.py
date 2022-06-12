sal = float(input('Escreva o salário atual R$ '))
if sal >= 1250:
    nsal = sal*1.1
    print('O novo salário é R$ {}'.format(nsal))
else:
    nsal = sal*1.15
    print('O novo salário é R$ {}'.format(nsal))
