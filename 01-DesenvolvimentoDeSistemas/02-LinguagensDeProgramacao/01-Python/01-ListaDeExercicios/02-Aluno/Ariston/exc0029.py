print("""
\033[1;37;44m 029) \033[m Crie um programa em PYTHON que: leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
quilômetro acima do limite.
""")
velocidade = float(input('Qual a velocidade do carro: '))
limite = 80
valor = 7.00
if velocidade > 80:
    multa=float(velocidade-limite)*valor
    print('\nVocê recebeu uma multa de : R$ {:.2f} pois andou {}Km/h acima da velocidade máxima de 80Km/h.\n'.format(multa,(velocidade-limite)))