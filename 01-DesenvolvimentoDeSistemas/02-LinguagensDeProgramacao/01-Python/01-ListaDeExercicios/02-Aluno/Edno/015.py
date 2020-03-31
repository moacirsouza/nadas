#(01-Gabarito/015.py)) Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

vlr_km = 0.15
vlr_dia = 60
km = float(input('Quantos KM o sr rodou? '))
dias = int(input('Quantos dias o sr passou com o veículo? '))

a_pagar = round((km*vlr_km) + (dias*vlr_dia),2)
print('')
print('.'*100)
print('')
print(' A Localiza agradece seu aluguel. O valor a pagar é R$ ' + str(a_pagar))
print('')
print('.'*100)