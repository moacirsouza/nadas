print("""
083) Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta.
""")

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
        print(f'{pilha}')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
            print(f'{pilha}')
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

# Outra forma - que achei mais simples de entender:

count1 = count2 = 0
x = str(input('Enter a expression: '))
for n in x:
    if '(' in n:
        count1 += 1
    elif ')' in n:
        count2 += 1
if count1 > count2:
    print('Expressão inválida!')
if count2 > count1:
    print('Expressão inválida!')
else:
    print('Sua expressão está válida')

