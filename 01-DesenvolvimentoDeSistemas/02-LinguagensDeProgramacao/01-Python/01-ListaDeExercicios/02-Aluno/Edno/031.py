# (01-Gabarito/031.py)) Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância em Km que você vai viajar? O Google Maps mostra: '))
print('')
preco = 0.45
if distancia <= 200:
    preco = 0.50

print('O valor da passagem é R$ ' + str(round(distancia*preco,2)))
