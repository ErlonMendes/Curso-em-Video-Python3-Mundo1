from random import randint
from time import sleep
num = int(input('Em que número entre 0 e 5 eu estou pensando? '))
alvo = randint(0, 5)
print('Processando...')
sleep(2)
if num == alvo:
    print('Acertou, eu pensei {}!'.format(alvo))
else:
    print('Errou, eu pensei {}!'.format(alvo))
