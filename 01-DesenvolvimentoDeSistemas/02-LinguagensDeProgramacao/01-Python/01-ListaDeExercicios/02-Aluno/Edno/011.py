# (01-Gabarito/011.py)) Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².


largura = float(input("Qual a largura da parede, patrão?\t"))
altura = float(input("Qual a altura da parede, patrão?\t"))

total = largura * altura
litros_necessarios = total/2

print('')
print('Patrão, o sr vai precisa de ' + str(litros_necessarios) + ' litros de tinta.')
print('Agora é só escolher a cor! :D')