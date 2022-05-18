num = input('Escreva um número entre 0 e 9999: ')
# print('unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}'.format(num[3], num[2], num[1], num[0]))
# Exige que o número tenha quatro caracteres

# alternativa numérica
num = int(num)
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}'.format(u, d, c, m))
