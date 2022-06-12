dist = int(input('Digite a distância da viagem (km): '))
if dist <= 200:
    preco = dist*0.50
else:
    preco = dist*0.45
# preco = dist*0.50 if dist <= 200 else dist*0.45
print('O custo da viagem é R$ {:.2f}'.format(preco))
