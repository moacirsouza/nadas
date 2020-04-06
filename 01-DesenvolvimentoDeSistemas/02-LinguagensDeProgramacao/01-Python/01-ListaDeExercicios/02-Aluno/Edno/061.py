# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# (01-Gabarito/051.py)) Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o termo da PA\t: '))
razao = int(input('Digite a razão da PA\t: '))
pa = termo;

print('')

print('a{} = {}'.format(1,termo))

i = 2
while i < 11:
#for i in range(2,11):
    pa = pa + razao
    print('a{} = {} + {} = {}'.format(i, termo, razao, pa))
    i = i+1

a10 = termo + (10-1) * razao
print('Conferindo com a fórmula an=a1+(n-1).r: a10={}+({}-1).{}:\t a10={}'.format(termo,10,razao,a10))