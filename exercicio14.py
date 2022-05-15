C = float(input('Digite a temperatura em °C '))
F = 32 + C*1.8
K = C + 273.15
R = K*1.8
print('{}°C = {:.1f}°F = {:.2f} K = {:.2f} R'.format(C, F, K, R))
