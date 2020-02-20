print('Ler quanto dinheiro tem na carteira e converter em Dólares Considere US$1,00=R$3,27 --]')
dinheiro = float(input('Quanto você tem na carteira em real? R$ '))
dolar = dinheiro / 3.27
print('\nCom {:.2f} reiais você consegue comprar {:.2f} dolares'.format(dinheiro,dolar))