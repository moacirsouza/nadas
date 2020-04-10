print("""
071) Crie um programa que simule o funcionamento de uma caixa eletrônico.
No início, pergutne ao usuário qual será o valor a ser sacado(número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS. Considere que o caixa possui cédulas de R$50, R$20, R$10
e R$1.
""")

print('=' * 30)
print('{:^30}'.format('BANCO RM'))
print('=' * 30)
valordosaque = int(input('Digite o valor a ser sacado: R$'))
total = valordosaque
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula +=1
    else:
        if totalcedula > 0:
            print('Total de {} cédulas de R${}'.format(totalcedula, cedula
        ))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
        
print('=' * 30)
print('Volte sempre !!!')


