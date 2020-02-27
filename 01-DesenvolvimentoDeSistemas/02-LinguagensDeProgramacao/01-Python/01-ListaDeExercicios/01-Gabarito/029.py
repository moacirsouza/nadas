print("""
029) Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
quilômetro acima do limite.
""")

### Entrada do programa: Recebe a velocidade do carro como um "float"
velocidade = float(input('Qual a velocidade do carro (Em Km/h): '))

### Definição das variáveis
limiteDeVelocidade = 80
custoPorQuilometroExcedido = 7

if velocidade > limiteDeVelocidade:
    multa = (velocidade-limiteDeVelocidade)*custoPorQuilometroExcedido
    print('\nVocê ultrapassou o limite de velocidade.\nSua multa é de R${:.2f}.\n'.format(multa))
else:
    print('\nParabéns. Você dirigiu dentro do limite de {}Km/h de velocidade.\n'.format(limiteDeVelocidade))
