print("""
005) Desafio 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor. 
""")
numero=int(input('Digite um número: '))
antecessor = numero-1
sucessor = numero+1
print('O antecessor do número {} é {}. Já o seu sucessor é {} '.format(numero,antecessor,sucessor))
