from random import choice
nome1 = input('Nome do aluno 1: ')
nome2 = input('Nome do aluno 2: ')
nome3 = input('Nome do aluno 3: ')
nome4 = input('Nome do aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O(A) escolhido(a) foi {}'.format(escolhido))
