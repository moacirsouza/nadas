print('[-- Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros --]\n')
metros = float(input('Informe um valor em metros: '))
decimetros  = metros*10
centimetros = metros*100
milimetros  = metros*1000
decametros  = metros/10
hectometros = metros/100
quilometros = metros/1000

print('\n+-------------------------------------------+')
print('| A medida informada em metros foi {}m'.format(metros))
print('| Em decímetros, ela equivale a {}dm'.format(decimetros))
print('| Em centrímetros, ela equivale a {}cm'.format(centimetros))
print('| Em milímetros, ela equivale a {}mm'.format(milimetros))
print('| Em decâmetros, ela equivale a {}dam'.format(decametros))
print('| Em hectômetros, ela equivale a {}hm'.format(hectometros))
print('| Em quilômetros, ela equivale a {}km'.format(quilometros))
print('+-------------------------------------------+')
