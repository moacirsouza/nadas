print("""
031) Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km
e R$0,45 para viagens mais longas.
""")

### Entrada do programa: Recebe a distância como um número real ("float").
distancia = float(input('Informe a distância que será percorrida na \
viagem (Em Km): '))

### Define o "custoPorQuilometro" como cinquenta centavos...
custoPorQuilometro = 0.5

### ...mas altera este valor, caso a distância seja maior que 200Km
if distancia > 200:
    custoPorQuilometro = 0.45

### O cálculo da passagem será sempre o produto da quantidade de quilômetros
### percorridos pelo custo por quilômetro. Este últiumo valor, no entanto,
### sempre receberá o valor correto, por causa da estrutura de decisão.
passagem = distancia*custoPorQuilometro

print('Sua passagem vai custar, aproximadamente, R${:.2f}.'.format(passagem))
