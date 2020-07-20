print("""
108) Adapte o código do desafio #107, criando uma função adicional chamada
moeda() que consiga mostrar os números como um valor monetário formatado.
""")

from utilidadesCeV import moeda

tamanhoDaBarra = 65
preco = 567
precoFormatado = moeda.moeda(preco)
incremento = 15
decremento = 25
precoIncrementado = moeda.moeda(moeda.aumentar(preco, incremento))
precoDecrementado = moeda.moeda(moeda.diminuir(preco, decremento))
precoDobrado = moeda.moeda(moeda.dobro(preco))
precoPelaMetade = moeda.moeda(moeda.metade(preco))

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
print('-'*tamanhoDaBarra)
