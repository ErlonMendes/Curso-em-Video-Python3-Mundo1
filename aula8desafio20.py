from random import shuffle
nome1 = input('Nome do aluno 1: ')
nome2 = input('Nome do aluno 2: ')
nome3 = input('Nome do aluno 3: ')
nome4 = input('Nome do aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação será: ', end='')
print(lista)
