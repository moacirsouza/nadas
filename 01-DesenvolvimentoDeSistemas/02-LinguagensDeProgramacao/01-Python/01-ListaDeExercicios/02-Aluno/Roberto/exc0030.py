print("""
029) Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
quilômetro acima do limite.
""")
velocidade = float(input('Velocidade de Veículo (Em Km/h): '))
if velocidade > 80:
    valordamulta = (velocidade - 80) * 7
    print('Você foi multado')
    print('O valor da multa foi: {:.2f}'.format(valordamulta)) 
else:
    print('Você está dentro dos limites de velocidade')


