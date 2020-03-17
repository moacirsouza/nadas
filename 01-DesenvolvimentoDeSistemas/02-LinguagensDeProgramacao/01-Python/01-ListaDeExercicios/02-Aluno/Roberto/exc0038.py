print("""
038) Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
""")
num1 = int(input('Digite o Primeiro Valor: ').strip())
num2 = int(input('Digite o Segundo Valor: ').strip())
if num1>num2:
    print('O Primeiro valor é maior')
elif num2>num1:
    print('O Segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')