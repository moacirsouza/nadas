#(01-Gabarito/012.py)) Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.


valor = float(input('Qual o preço do Bolo Formigueiro sem glutem, sem açúcar, sem gosto? '))

print('Valor com desconto: ' + str(round(valor*0.95, 2)))
