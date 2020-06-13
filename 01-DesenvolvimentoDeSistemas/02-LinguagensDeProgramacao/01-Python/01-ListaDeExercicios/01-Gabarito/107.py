print("""
107) Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e
use algumas dessas funções.
""")

### O truque aqui foi transformar o diretório "modulos" em um
### pacote e para fazer isso, basta inserir o arquivo "__init__.py"
### dentro dele. O arquivo pode ser vazio, só de existir já indica
### ao Python que aquele diretório é um pacote.
from utilidadesCeV import moeda

tamanhoDaBarra = 65
preco = 567
incremento = 15
decremento = 25
precoIncrementado = moeda.aumentar(preco, incremento)
precoDecrementado = moeda.diminuir(preco, decremento)
precoDobrado = moeda.dobro(preco)
precoPelaMetade = moeda.metade(preco)


print('-'*tamanhoDaBarra)
print(f'{"Os valores informados foram":^{tamanhoDaBarra}}')
print(f"""
Preço: {preco}
Taxa de incremento: {incremento}%
Taxa de redução: {decremento}%""")
print('-'*65)
print(f'O valor {preco}, ao sofrer um aumento de {incremento}% fica igual a {precoIncrementado}.')
print(f'O valor {preco}, ao sofrer uma reducao de {decremento}% fica igual a {precoDecrementado}.')
print(f'O dobro do preço {preco} é {precoDobrado}.')
print(f'A metade do valor {preco} é {precoPelaMetade}.')
