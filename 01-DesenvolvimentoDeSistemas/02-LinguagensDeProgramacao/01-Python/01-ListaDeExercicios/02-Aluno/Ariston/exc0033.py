print("""
\033[1;37;44m 033) \033[m Crie um programa em PYTHON que: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
""") 
numero01=float(input('Digite o numero01: '))
numero02=float(input('Digite o numero02: '))
numero03=float(input('Digite o numero03: '))

lista=[numero01,numero02,numero03]
lista.sort()
print('\nO menorr número é {} e o maior é {}.\n'.format(lista[0],lista[2]))
