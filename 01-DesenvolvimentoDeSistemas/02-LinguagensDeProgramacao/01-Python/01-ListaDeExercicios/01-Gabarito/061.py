print("""
061) Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
""")

primeiroTermo = int(input('Informe o primeiro termo da PA: ').strip())
razao = int(input('Informe a razão da PA: ').strip())

termo = primeiroTermo
contador = 0
termosDaPA = ''

while contador < 10:
    termosDaPA += '{}, '.format(termo)
    termo += razao
    contador += 1

mensagemFinal = """
Os 10 primeiros termos da PA são: {}""".format(termosDaPA[:-2])

print(mensagemFinal)
