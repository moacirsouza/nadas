print("""
\033[1;37;44m 030) \033[m Crie um programa em PYTHON que: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
""")
numero = int(input('Digite um número inteiro: '))
if (numero%2)==0:
    print('\nO número {} é par'.format(numero))
else:
    print('\nO número {} é impar'.format(numero))