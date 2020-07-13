print("""
102) Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e outro chamado
show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.
""")

def fatorial(numero, show=False):

    fatorial = 1
    processoDeCalculo = []

    if numero == 0:
        fatorial = 1
        processoDeCalculo.append(fatorial)
    
    if numero < 0:
        return 'ERRO: Não existe fatorial de números negativos.'
    
    while numero >= 1:
        fatorial *= numero
        processoDeCalculo.append(numero)
        numero -= 1
    
    resposta = fatorial
    
    if show:
        resposta = ' x '.join(map(str, processoDeCalculo)) + f' = {fatorial}'
    
    return resposta


entrada = int(input('Escolha um número inteiro para mostrar o fatorial: '))

while True:
    escolha = input('Deseja mostrar o processo de \
cálculo? (s/n) ').strip().lower()

    if escolha == 's' or escolha == 'n':
        break

    print('Use apenas S/s ou N/n para informar sua escolha.')

show = False

if escolha == 's':
    show=True

print(f'O fatorial de {entrada} é: {fatorial(entrada, show)}')
