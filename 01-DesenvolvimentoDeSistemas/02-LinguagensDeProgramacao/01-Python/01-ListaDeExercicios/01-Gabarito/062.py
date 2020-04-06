print("""
062) Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.
""")

primeiroTermo = int(input('Informe o primeiro termo da PA: ').strip())
razao = int(input('Informe a razão da PA: ').strip())

termo = primeiroTermo
contador = 0
termosDaPA = ''
quantidadeDeTemosDaPA = 10
condicaoDeSaida = 1

while condicaoDeSaida != 0:
    while contador < quantidadeDeTemosDaPA:
        termosDaPA += '{},'.format(termo)
        termo += razao
        contador += 1
    if contador == 10:
        print('Os 10 primeiros termos da PA são: {}'.format(termosDaPA[:-1]))
    else:
        print('Os próximos {} termos da PA são: {}'.format(condicaoDeSaida,termosDaPA[:-1]))
    condicaoDeSaida = int(input('Quantos termos a mais você quer imprimir? (0 para sair): ').strip())
    termosDaPA = ''
    quantidadeDeTemosDaPA += condicaoDeSaida
print('Progressão finalizada com {} termos mostrados.'.format(contador))
