print ('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\n')
produto = float(input('Qual o preço do produto: '))
produto = (produto*0.95)
print('\nO Valor do produto com 5% de Desconto é R$ {:.2f}.'.format(produto))