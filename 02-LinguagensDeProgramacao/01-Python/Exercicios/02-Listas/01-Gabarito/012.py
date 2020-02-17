print('[-- Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. --]\n')
precoDoProduto = float(input('Informe o preço do produto: R$ '))
desconto = 0.05
precoFinal = precoDoProduto-(precoDoProduto*desconto)
print('O preço final do produto, com 5% de desconto, é R$ {:.2f}'.format(precoFinal))
