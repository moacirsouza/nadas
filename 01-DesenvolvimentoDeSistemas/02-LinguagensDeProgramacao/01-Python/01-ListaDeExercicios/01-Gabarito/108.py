print("""
108) Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
""")

from utilidadesCeV import moeda

tamanhoDaBarra = 65
preco = 567
precoFormatado = moeda.moeda(567)
incremento = 15
decremento = 25
precoIncrementado = moeda.moeda(moeda.aumentar(preco, incremento))
precoDecrementado = moeda.moeda(moeda.diminuir(preco, decremento))
precoDobrado = moeda.moeda(moeda.dobro(preco))
precoPelaMetade = moeda.moeda(moeda.metade(preco))

print('-'*tamanhoDaBarra)
print(f'{"Os valores informados foram":^{tamanhoDaBarra}}')
print(f"""
Preço: {precoFormatado}
Taxa de incremento: {incremento}%
Taxa de redução: {decremento}%""")
print('-'*tamanhoDaBarra)

print(f'O valor {precoFormatado}, ao sofrer um aumento de {incremento}%, fica igual a {precoIncrementado}.')
print(f'O valor {precoFormatado}, ao sofrer uma reducao de {decremento}%, fica igual a {precoDecrementado}.')
print(f'O dobro do preço {precoFormatado} é {precoDobrado}.')
print(f'A metade do valor {precoFormatado} é {precoPelaMetade}.')
print('-'*tamanhoDaBarra)
