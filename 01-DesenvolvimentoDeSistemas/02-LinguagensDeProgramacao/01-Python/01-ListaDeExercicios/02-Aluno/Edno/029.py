#(01-Gabarito/029.py)) Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada quilômetro acima do limite.

velocidade = float(input('Qual foi a velocidade registrada para esse veículo no nosso radar super sônico? '))

if velocidade > 80:
    multa = velocidade - 80
    multa = multa * 7
    print('Senhor, o senhor passou aqui a ' + str(velocidade) + 'Km/h. O senhor será multado em R$ ' + str(round(multa,2)))

print('')
print('Boa viagem. Siga com cuidado.')