print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.')
print(' Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.\n')
quilometro = int(input('Quantos quilometros o carro andou: '))
dias = int(input('Por quantos dias o carro foi alugado: '))
pagar = (dias*60)+(quilometro*0.15)
print('Apos ficar com o carro {} dias e ter percorrido {} Km, você só vai pagar R$ {:.2f}.'.format(dias,quilometro,pagar))