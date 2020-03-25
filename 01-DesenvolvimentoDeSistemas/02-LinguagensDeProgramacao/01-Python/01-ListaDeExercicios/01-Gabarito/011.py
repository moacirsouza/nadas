print("""
011) Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m² 
""")
altura = float(input('Informe a altura da parede (Em metros): '))
largura = float(input('Informe a largura da parede (Em metros): '))
area = altura*largura
areaCobertaPorUmLitroDeTinta = 2
quantidadeFinalDeTinta = (area)/areaCobertaPorUmLitroDeTinta
print('\nA área da parede é de {:.2f}m²'.format(area))
print('Para pintá-la é preciso, aproximadamente, {:.2f}l de tinta.'.format(quantidadeFinalDeTinta))
