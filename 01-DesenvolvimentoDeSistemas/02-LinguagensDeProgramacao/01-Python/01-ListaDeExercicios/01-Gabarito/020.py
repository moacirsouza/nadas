print("""
020) O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 
""")
from random import shuffle
nome01 = input('Informe o primeiro nome: ')
nome02 = input('Informe o segundo nome: ')
nome03 = input('Informe o terceiro nome: ')
nome04 = input('Informe o quarto nome: ')

alunos = [nome01,nome02,nome03,nome04]
shuffle(alunos)

print(alunos)
