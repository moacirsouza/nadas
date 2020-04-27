print("""
082) Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras, que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
""")

listaDeNumeros = []
listaDeNumerosPares = []
listaDeNumerosImpares = []

while True:
    numero = int(input('Digite um número: ').strip())
    listaDeNumeros.append(numero)

    if numero%2 == 0:
        listaDeNumerosPares.append(numero)
    else:
        listaDeNumerosImpares.append(numero)

    while True:
        querContinuar = input('Deseja continuar? (s/n) ').strip().lower()

        if querContinuar == 's' or querContinuar == 'n':
            break
        print('ATENÇÃO: Digite S/s ou N/n, respectivamente, para continuar ou sair do programa.')

    if querContinuar == 'n':
        break

print(f'Lista dos números PARES: {listaDeNumerosPares}')
print(f'Lista dos números ÍMPARES: {listaDeNumerosImpares}')
print(f'Lista com todos os números: {listaDeNumeros}')
