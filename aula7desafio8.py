dist = float(input('Digite a distância (m) '))
km = dist/1e3
hm = dist/1e2
dam = dist/10
dm = dist*10
cm = dist*1e2
mm = dist*1e3
ft = dist*3.28084
inch = dist*39.3701
print('{} m = {} km = {} hm = {} dam = {} dm = {} cm = {} mm = {} ft = {} in'
      .format(dist, km, hm, dam, dm, cm, mm, ft, inch))
