print("""
109) Modifique as funções que foram criadas no desafio 107 para que elas
aceitem um parâmetro a mais, informando se o valor retornado por elas vai
ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
""")

from utilidadesCeV import moeda

tamanhoDaBarra = 65
preco = 789
precoFormatado =  moeda.moeda(preco)
incremento = 15
decremento = 25
precoIncrementado = moeda.aumentar(preco, incremento, True)
precoDecrementado = moeda.diminuir(preco, decremento, True)
precoDobrado = moeda.dobro(preco, True)
precoPelaMetade = moeda.metade(preco, True)


print('-'*tamanhoDaBarra)
print(f'{"Os valores informados foram":^{tamanhoDaBarra}}')
print('-'*tamanhoDaBarra)
print(f"""Preço: {precoFormatado}
Taxa de incremento: {incremento}%
Taxa de redução: {decremento}%""")
print('-'*tamanhoDaBarra)
print(f'{"Resultados":^{tamanhoDaBarra}}')
print('-'*tamanhoDaBarra)
print(f'Um aumento de {incremento}% resulta em {precoIncrementado}.')
print(f'Uma reducao de {decremento}% resulta em {precoDecrementado}.')
print(f'O dobro de {precoFormatado} é {precoDobrado}.')
print(f'A metade de {precoFormatado} é {precoPelaMetade}.')
