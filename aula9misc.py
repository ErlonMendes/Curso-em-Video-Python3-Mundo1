frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
dividido = frase.split()
print(dividido)
print('-'.join(dividido))
frase2 = '    Curso em Vídeo Python    '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
print("""Engenharia-Quimica-MATLAB possui as minhas principais produções em
ensino e pesquisa de Engenharia Química em MATLAB.""")
