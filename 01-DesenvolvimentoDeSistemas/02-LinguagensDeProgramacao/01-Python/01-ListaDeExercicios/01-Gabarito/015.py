print("""
015) Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado. 
""")
diasDeLocacao = int(input('Por quantos dias o carro foi alugado? '))
quilometrosRodados = float(input('Quantos quilômetros foram percorridos? '))
custoDaLocacaoDiaria = 60
custoPorQuilometroRodado = 0.15
custoFinal = (diasDeLocacao*custoDaLocacaoDiaria) + (quilometrosRodados*custoPorQuilometroRodado)
print('Um carro alugado por {} dia(s) e que rodou {} Km, custa um total de R$ {:.2f}'.format(diasDeLocacao,quilometrosRodados,custoFinal))
