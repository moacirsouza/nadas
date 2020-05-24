print("""
098) Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
através da função criada:

A) de 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) uma contagem personalizada
""")

def contador():
    print(f'Contagem de 1 até 10 (Sem temporização): {list(range(1,11))}')
    print(f'Contagem de 10 a 0, de 2 em 2 (Sem temporização): {list(range(10,-1,-2))}')

    ### Contagem personalizada
    inicio = int(input('Início: ').strip())
    fim = int(input('Fim: ').strip())
    passo = int(input('Passo: ').strip())

    ### Se o passo for 0, é preciso forçá-lo a receber o valor 1
    if passo == 0:
        passo = 1

    ### Se o valor de "inicio" for maior que o de "fim", o valor de "passo"
    ### PRECISA ser negativo. No entanto, se o "passo" já for um número
    ### negativo, o conteúdo original permanece
    if inicio > fim and passo*(-1) < passo:
        passo *= -1

    ### Para que a contagem vá até o valor de "fim", informado pelo usuário
    ### é preciso incrementá-lo com o valor de "passo", uma vez que o
    ### intervalo final de "range()" é "aberto"
    for numero in range(inicio, fim+passo, passo):
        print(numero, end=' ')
    print('')

contador()
