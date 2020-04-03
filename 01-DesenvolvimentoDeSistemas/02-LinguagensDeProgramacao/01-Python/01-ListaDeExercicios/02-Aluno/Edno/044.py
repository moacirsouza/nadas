# (01-Gabarito/044.py)) Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#       - À vista dinheiro/cheque: 10% de desconto
#       - À vista no cartão: 5% de desconto
#       - Em até 2x no cartão: Preço normal
#       - 3x ou mais no cartão: 20% de juros

preco = float(input('A como é o abacaxi? '))
av = round(preco * 0.9,2)
avcartao = round(preco * 0.95,2)
v2 = round(preco * 0.5,2)
v3 = round(((preco * 1.2) / 3),2)

print('')
print('É R$ {}, freguês. Veja a tabela de preços:'.format(preco))

print('À Vista (Dinheiro/Cheque)\t\tÀ Vista (Cartão)\t\t2X sem juros\t\t3X com juros(20%)')
print('\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}'.format(av, avcartao, v2, v3))
