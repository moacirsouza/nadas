print("""
003) Crie um programa que leia dois números e mostre a soma entre eles.
""")

numero01=int(input('Digite o número 01: '))
numero02=int(input('Digite o número 02: '))

soma=numero01+numero02

print('\n[Colocando a soma diretamente no .format] A soma dos números é \
{}'.format(numero01+numero02))

print('\n[Usando uma variável intermediária] A soma dos números é \
{}'.format(soma))
