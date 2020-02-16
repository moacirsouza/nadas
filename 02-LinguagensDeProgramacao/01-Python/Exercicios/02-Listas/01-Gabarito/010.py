print('[-- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00=R$3,27 --]\n')
reais = float(input('Quantos reais você tem? '))
taxaDeCambio = 3.27
dolares = reais/taxaDeCambio
print('Com R$ {} e a cotação atual de US$ 1,00 = R$ {}, é possível comprar {:.2f} dólares.'.format(reais, taxaDeCambio, dolares))
