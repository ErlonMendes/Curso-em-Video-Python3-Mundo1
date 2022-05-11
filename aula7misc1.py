print(5**4)
print(pow(5, 4))
print('Oi'*10)
print('='*10)
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}!'.format(nome))  # Com 20 caracteres
print('Prazer em te conhecer, {:>20}!'.format(nome))  # Com 20 caracteres alinhado a direita
print('Prazer em te conhecer, {:<20}!'.format(nome))  # Com 20 caracteres alinhado a esquerda
print('Prazer em te conhecer, {:^20}!'.format(nome))  # Com 20 caracteres centralizado
print('Prazer em te conhecer, {:_^20}!'.format(nome))  # Com 20 caracteres centralizado e vazios preenchidos com _
