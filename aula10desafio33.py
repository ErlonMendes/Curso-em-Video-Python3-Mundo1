n1 = int(input('Escreva n1: '))
n2 = int(input('Escreva n2: '))
n3 = int(input('Escreva n3: '))
# Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('{} é o menor número'.format(menor))
print('{} é o maior número'.format(maior))
