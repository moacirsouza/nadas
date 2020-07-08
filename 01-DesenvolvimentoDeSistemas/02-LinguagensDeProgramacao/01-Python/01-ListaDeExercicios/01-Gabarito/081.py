print("""
081) Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
""")

listaDeNumeros = []

while True:
    numero = int(input('Digite um número: ').strip())
    listaDeNumeros.append(numero)

    while True:
        querContinuar = input('Deseja continuar? (s/n) ').strip().lower()

        if querContinuar == 's' or querContinuar == 'n':
            break
        
        print('ATENÇÃO: Digite S/s ou N/n, respectivamente, para continuar \
ou sair do programa.')

    if querContinuar == 'n':
        listaDeNumeros.sort(reverse=True)
        nao = ' '
        
        if 5 not in listaDeNumeros:
            nao = ' não '

        cincoEstaNaLista = f'O número 5{nao}está na lista.'
        break

print(f'A quantidade de números digitados foi {len(listaDeNumeros)}')
print(f'A lista, em ordem decrescente, é: {listaDeNumeros}')
print(f'{cincoEstaNaLista}')
