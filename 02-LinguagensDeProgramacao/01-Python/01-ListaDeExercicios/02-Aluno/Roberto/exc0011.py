print('[-- Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m² --]\n')
largura = float(input('Qual a largura da parede (em metros)? '))
altura = float(input('Qual a altura da parede (em metros)? '))
area = largura*altura
qtdedetinta = area/2
print ('A área da parede é {:.2f}m² e a quantidade de tinta para pintar a parede é de {:.2f}m² ' .format(area, qtdedetinta))



