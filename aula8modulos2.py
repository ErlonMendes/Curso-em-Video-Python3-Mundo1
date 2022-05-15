from math import sqrt, ceil, floor  # importou apenas as funções que solicitei do módulo de matemática
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('raiz({}) = {:.3f}'.format(num, raiz))
print('raiz({}) = {}'.format(num, ceil(raiz)))
print('raiz({}) = {}'.format(num, floor(raiz)))
