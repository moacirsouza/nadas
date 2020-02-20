print('[-- Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros --]\n')
metro = float(input('Digite o valor em metros: '))
km = metro/1000
hm = metro/100
dam = metro/10
dm = metro*10
cm = metro*100
mm = metro*1000
print('A medida de {} metro(s) equivale(m) a {} km, {}hm, {}dam, {}dm, {}cm, {}mm' .format(metro,km,hm,dam,dm,cm,mm))


