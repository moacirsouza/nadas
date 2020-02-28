# Converta metros em centímetros e milímetros
metro = float(input('Quantos metros: '))
klm = metro/1000
hkm = metro/100
dac = metro/10
dem = metro*10
cem = metro*100
mim = metro*1000
print('Metros : {}m, Kilometros: {}km, Hectômetros: {}hm, Decâmetros: {}dam, Decímetros: {}dm, Centímetros: {}cm,  Milímetros: {}mm' .format(metro,klm,hkm,dac,dem,cem,mim))
