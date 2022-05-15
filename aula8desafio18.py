from math import sin, cos, tan, radians
ang = float(input('Digite um ángulo em graus: '))
print('sen({}) = {:.3f} \ncos({}) = {:.3f} \ntan({}) = {:.3f}'
      .format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))
