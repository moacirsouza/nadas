print("""
078) Faça um programa que leia 5 valores numéricos de guarde-os em uma
lista. No final, mostre qual foi o maior e o menor valor digitado e suas
respectivas posições na lista.
""")

listaComCincoValores = []

for numero in range(1, 6):
    mensagemDeEntrada = f'Informe o {numero}º número (Posição {numero-1}): '
    entrada = int(input(mensagemDeEntrada))
    listaComCincoValores += [entrada]

maiorNumero = max(listaComCincoValores)
menorNumero = min(listaComCincoValores)

posicoesDosMenores = ''
for posicao, numero in enumerate(listaComCincoValores):
    if numero == menorNumero:
        posicoesDosMenores += str(posicao) + ', '

posicoesDosMaiores = ''
for posicao, numero in enumerate(listaComCincoValores):
    if numero == maiorNumero:
        posicoesDosMaiores += str(posicao) + ', '

print(f"""
O menor número da lista é {menorNumero}.
Ele pode ser encontrado na(s) posição(ões): {posicoesDosMenores[:-2]}.""")
print(f"""
O maior número da lista é {maiorNumero}.
Ele pode ser encontrado na(s) posição(ões): {posicoesDosMaiores[:-2]}.""")
