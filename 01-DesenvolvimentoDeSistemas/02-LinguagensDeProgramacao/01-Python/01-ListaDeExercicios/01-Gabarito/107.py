print("""
107) Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e
use algumas dessas funções.
""")

### Esse é o "truque" para importar modulos de um local fixo
### Referência: https://do.co/2XuLGEN
# import sys
# sys.path.append('modulos')
from modulos import moeda


preco = 567
incremento = 15
decremento = 25
precoIncrementado = moeda.aumentar(preco, incremento)
precoDecrementado = moeda.diminuir(preco, decremento)
precoDobrado = moeda.dobro(preco)
precoPelaMetade = moeda.metade(preco)

print(f'O valor {preco}, ao sofrer um aumento de {incremento}% fica igual a {precoIncrementado}.')
print(f'O valor {preco}, ao sofrer uma reducao de {decremento}% fica igual a {precoDecrementado}.')
print(f'O dobro do preço {preco} é {precoDobrado}.')
print(f'A metade do valor {preco} é {precoPelaMetade}.')