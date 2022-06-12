nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2)/2
if media >= 7:
    print('Sua média é {:.1f} e você está aprovado'.format(media))
else:
    print('Sua média é {:.1f} e você está reprovado'.format(media))
print('FIM')
