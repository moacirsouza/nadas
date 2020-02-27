print ('Fazer programa que ler a largura e a altura de uma parede em metros e calcula a sua área e a quantidade de tinta necessária para pintá-la, 1 litro de tinta, pinta uma área de 2m² ')
print()

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area=altura * largura
quantidade = area/2
print('para uma parede de área {:.2f}m², nós usamos {:.2f} litros de tinta'.format(area,quantidade))