print("""
079) Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.
""")

listaDeNumeros = []

while True:
    numero = int(input('Digite um número: ').strip())

    if numero in listaDeNumeros:
        print(f'O número {numero} já está na lista. Não posso adicioná-lo.')
    else:
        listaDeNumeros += [numero]

    while True:
        continuar = input('Deseja continuar? (s/n) ').strip().lower()
        if continuar == 's' or continuar == 'n':
            break
        print('Digite S/s para continuar ou N/n para sair.')

    if continuar == 'n':
        listaDeNumeros.sort()
        break

print(f'\nSua lista de números foi: {listaDeNumeros}')
