# (01-Gabarito/045.py)) Crie um programa que faça o computador jogar Jokenpô com você.

from random import  randint

moves = [0,1,2] # 0-pedra, 1-papel, 2-tesoura
values=['Pedra', 'Papel', 'Tesoura']
print('''I'M "PAPER HEAD," THE FIRST HENCHMAN OF THE KING.''')
print('''I'LL LET YOU PASS BY HERE IF YOU WIN ONE "JANKEN" MATCHES.''')
print('')

pc_turn = randint(0, 2)
my_turn = int(input('Escolha:\n'
                    '\t1 para pedra\n'
                    '\t2 para papel\n'
                    '\t3 para tesoura\t'))

my_turn = my_turn-1

#print('PC: {}, Eu: {}'.format(values[pc_turn],values[my_turn]))
if pc_turn == my_turn:
    print('PC: {}, Usuário: {} - Empate'.format(values[pc_turn], values[my_turn]))
    print("It's a tie!")
else:
    if (pc_turn == 0 and my_turn == 1):
        print('PC: {}, Usuário: {} - PC Vence'.format(values[pc_turn], values[my_turn]))
    elif (pc_turn == 1 and my_turn == 0):
        print('PC: {}, Usuário: {} - Usuário Vence'.format(values[pc_turn], values[my_turn]))
    elif pc_turn < my_turn:
        if my_turn == 0 and pc_turn == 1:
            print('PC: {}, Usuário: {} - Usuário Vence'.format(values[pc_turn], values[my_turn]))
        else:
            print('PC: {}, Usuário: {} - PC Vence'.format(values[pc_turn], values[my_turn]))
    else:
        print('PC: {}, Usuário: {} - Usuário Vence'.format(values[pc_turn], values[my_turn]))





