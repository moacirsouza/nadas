print("""
060) Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5!=5x4x3x2x1=120
""")

numero = int(input('Informe o número: ').strip())
contador = numero
fatorial = 1
esqueletoDoFatorial = ''

while contador >= 1:
    fatorial *= contador
    esqueletoDoFatorial += '{} x '.format(contador, end='')
    contador -=1

### A variável "esqueletoDoFatorial" foi passada com o fatiamento
### [:-3] a fim de remover o último "x", inserido quando ela foi
### criada.
mensagemFinal = """
O fatorial é: {}! = {} = {}
""".format(numero,
           esqueletoDoFatorial[:-3],
           fatorial)

print(mensagemFinal)
