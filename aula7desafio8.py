dist = float(input('Digite a distância (m) '))
centi = dist*1e2
mili = dist*1e3
foot = dist*3.28084
inch = dist*39.3701
print('{} m = {} cm = {} mm = {} ft = {} in'.format(dist, centi, mili, foot, inch))
