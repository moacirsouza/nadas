# (01-Gabarito/010.py)) Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# Dólares ela pode comprar. Considere US$1,00=R$3,27.

cotacao_dolar = 3.27
dinheiro = float(input('Ei, mano! Perdeu! Quanto é que tem nessa carteira velha?\t'))
print('')
print('Massa! Com essa grana posso comprar ' + str(round(dinheiro/cotacao_dolar,2)) + ' dolares!!! Estou rico!')