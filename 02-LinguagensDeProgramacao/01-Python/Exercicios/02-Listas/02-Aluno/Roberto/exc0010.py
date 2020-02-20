print('[-- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00=R$3,27 --]\n')
reais = float(input('Quanto você tem de dinheiro? R$ '))
dolar = reais/3.27
print('Com R${}, você poderá comprar ${:.2f} ' .format(reais, dolar))

