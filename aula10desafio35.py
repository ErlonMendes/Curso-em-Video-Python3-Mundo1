r1 = float(input('Aresta r1: '))
r2 = float(input('Aresta r2: '))
r3 = float(input('Aresta r3: '))
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Estas três arestas não podem formar um triângulo!')
else:
    print('Estas três arestas podem formar um triângulo!')
