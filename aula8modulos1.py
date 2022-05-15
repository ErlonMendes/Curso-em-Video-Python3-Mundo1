import math  # importou todas as funções do módulo de matemática
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('raiz({}) = {:.3f}'.format(num, raiz))
print('raiz({}) = {}'.format(num, math.ceil(raiz)))
print('raiz({}) = {}'.format(num, math.floor(raiz)))
