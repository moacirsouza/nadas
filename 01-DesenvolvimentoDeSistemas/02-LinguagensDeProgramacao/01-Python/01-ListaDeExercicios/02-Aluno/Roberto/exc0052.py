print("""
052) Faça um programa que leia um número inteiro e diga se
ele é ou não um número primo.
""")
total = 0
numero = int(input('Digite um número: '))
for contador in range (1, numero + 1):
     if numero % contador == 0:
        total += 1
print('O número {} foi divisível {} vezes'.format(numero, total))
if total ==  2:
    print('O número {} é primo ! '.format(numero))
else:
    print('O número {} não é primo !'.format(numero))




