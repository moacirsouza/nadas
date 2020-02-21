print('[-- Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado. --]\n')
kmpercorridos = float(input('Qual a quantidade de km percorridos? '))
qtdedediasalugados = int(input('Qual a quantidade de dias alugados? '))
custodiario = 60
custoporkmrodado = 0.15
valorapagar = (kmpercorridos*custoporkmrodado) + (qtdedediasalugados*custodiario)
print('O valor a pagar por {} dias alugados e {} km percorridos é: R${} ' .format(qtdedediasalugados, kmpercorridos, valorapagar))
