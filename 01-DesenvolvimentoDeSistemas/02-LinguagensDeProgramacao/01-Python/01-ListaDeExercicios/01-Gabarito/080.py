print("""
080) Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a
lista ordenada na tela.
""")

listaComCincoNumeros = []
maior = menor = 0

for indice in range(0, 5):
    entrada = int(input(f'Informe o {indice+1}º número: '))

    if indice == 0:
        maior = menor = entrada
        listaComCincoNumeros.append(entrada)
    else:
        if entrada > maior:
            maior = entrada
            listaComCincoNumeros.append(entrada)
        elif entrada < menor:
            menor = entrada
            listaComCincoNumeros.insert(0, entrada)
        else:
            for k, v in enumerate(listaComCincoNumeros):
                if entrada > listaComCincoNumeros[k] and entrada < listaComCincoNumeros[k+1]:
                    listaComCincoNumeros.insert(k+1, entrada)

print(listaComCincoNumeros)
