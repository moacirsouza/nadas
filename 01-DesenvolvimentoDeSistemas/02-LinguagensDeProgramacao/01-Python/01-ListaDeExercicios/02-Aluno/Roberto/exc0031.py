print("""
031) Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.
""")
distancia = float(input('Digite a distância da viagem (em Km):'))

if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
print('O preço da passagem será: {:.2f}'.format(preco))
