frase = input('Escreva uma frase: ').strip()
print('A frase possui {} ocorrência(s) da letra "A"'.format(frase.upper().count('A')))
print('A primeira ocorrência de "A" é em {}'.format(frase.upper().find('A')))
print('A última ocorrência de "A" é em {}'.format(frase.upper().rfind('A')))
