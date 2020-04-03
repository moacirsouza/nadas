# (01-Gabarito/037.py)) Escreva um programa que leia um número inteiro qualquer e peça ao usuário para escolher qual
# será a base de conversão:
#       - 1 para binário
#       - 2 para octal
#       - 3 para hexadecimal


numero = int(input('Qual é o número? \t\t\t'))
opcao = int(input('Pra que base eu converto o número '+str(numero)+'? \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \t\t\t'))


if opcao == 1:
    print('O binário de {} é {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('O octal de {} é {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('O hexadecimal de {} é {}'.format(numero, hex(numero)))
else:
    print('Seu jegue!!!! Respeita a opção!!!')

