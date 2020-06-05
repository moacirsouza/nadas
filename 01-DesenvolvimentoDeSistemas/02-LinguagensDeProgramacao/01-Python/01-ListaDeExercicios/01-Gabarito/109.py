print("""
109) Modifique as funções que foram criadas no desafio 107 para que elas aceitem um
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado
pela função moeda(), desenvolvida no desafio 108.
""")

from modulos import moeda

tamanhoDaBarra = 65
preco = 567
precoFormatado =  moeda.moeda(567)
incremento = 15
decremento = 25
precoIncrementado = moeda.aumentar(preco, incremento, True)
precoDecrementado = moeda.diminuir(preco, decremento, True)
precoDobrado = moeda.dobro(preco, True)
precoPelaMetade = moeda.metade(preco, True)


print('-'*tamanhoDaBarra)
print(f'{"Os valores informados foram":^{tamanhoDaBarra}}')
print(f"""
Preço: {precoFormatado}
Taxa de incremento: {incremento}%
Taxa de redução: {decremento}%""")
print('-'*65)
print(f'O valor {precoFormatado}, ao sofrer um aumento de {incremento}%, fica igual a {precoIncrementado}.')
print(f'O valor {precoFormatado}, ao sofrer uma reducao de {decremento}%, fica igual a {precoDecrementado}.')
print(f'O dobro do preço {precoFormatado} é {precoDobrado}.')
print(f'A metade do valor {precoFormatado} é {precoPelaMetade}.')
