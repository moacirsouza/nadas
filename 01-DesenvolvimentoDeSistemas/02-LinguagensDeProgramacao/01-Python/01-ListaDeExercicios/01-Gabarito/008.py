print("""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros 
""")
metros = float(input('Informe um valor em metros: '))
decimetros  = metros*10
centimetros = metros*100
milimetros  = metros*1000
decametros  = metros/10
hectometros = metros/100
quilometros = metros/1000

print('\n+'+('-'*50)+'+')
print('| A medida informada em metros foi: {:.> 12,.2f} m |'.format(metros))
print('| Em decímetros, ela equivale a: {:.> 14,.2f} dm |'.format(decimetros))
print('| Em centrímetros, ela equivale a: {:.> 12,.2f} cm |'.format(centimetros))
print('| Em milímetros, ela equivale a: {:.> 14,.2f} mm |'.format(milimetros))
print('| Em decâmetros, ela equivale a: {:.> 13,.2f} dam |'.format(decametros))
print('| Em hectômetros, ela equivale a: {:.> 13,.2f} hm |'.format(hectometros))
print('| Em quilômetros, ela equivale a: {:.> 13,.2f} km |'.format(quilometros))
print('+'+('-'*50)+'+\n')
