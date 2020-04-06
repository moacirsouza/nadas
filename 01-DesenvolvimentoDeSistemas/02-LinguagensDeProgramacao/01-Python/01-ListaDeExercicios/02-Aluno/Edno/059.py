# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela.
# Seu programa deverá realizar a operação solicitada em cada caso.
#       - \[1\] somar
#       - \[2\] multiplicar
#       - \[3\] maior
#       - \[4\] novos números
#       - \[5\] sair do programa

opcao = 0
novos_numeros = True
while opcao != 5:
    if novos_numeros:
        numero1 = float(input('Digite o 1º número\t: '))
        numero2 = float(input('Digite o 2º número\t: '))
        novos_numeros = False

    print('')
    print('Escolha a operação ou sair')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    print('')
    opcao = int(input(''))

    if opcao == 1:
        print('A soma de {} + {} é igual a {}'.format(numero1, numero2, numero1+numero2))
    elif opcao == 2:
        print('{} multiplicado por {} é igual a {}'.format(numero1, numero2, numero1*numero2))
    elif opcao == 3:
        if numero1 > numero2:
            print('{} é maior que {}'.format(numero1, numero2))
        else:
            print('{} é maior que {}'.format(numero2, numero1))
    elif opcao == 4:
        novos_numeros = True

