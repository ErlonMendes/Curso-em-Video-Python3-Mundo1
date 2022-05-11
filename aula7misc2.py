n1 = int(input('Digite um número inteiro '))
n2 = int(input('Digite outro número inteiro '))
som = n1+n2
sub = n1-n2
prod = n1*n2
div = n1/n2
dint = n1//n2
pot = n1**n2
# print('{} + {} = {}'.format(n1, n2, som))
# print('{} - {} = {}'.format(n1, n2, sub))
# print('{} x {} = {}'.format(n1, n2, prod))
# print('{} / {} = {:.3f}'.format(n1, n2, div))
# print('{} divisão inteira por {} = {}'.format(n1, n2, dint))
# print('{}^{} = {}'.format(n1, n2, pot))
print('{} + {} = {} \n{} - {} = {} \n{} x {} = {} \n{} / {} = {:.3f} \n{} divisão inteira por {} = {} \n{}^{} = {}'
      .format(n1, n2, som, n1, n2, sub, n1, n2, prod, n1, n2, div, n1, n2, dint, n1, n2, pot))
print('{} + {} = {}'.format(n1, n2, som), end=' e ')  # Faz o próximo print sem quebrar a linha
print('{} - {} = {}'.format(n1, n2, sub))
