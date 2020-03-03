print('[-- Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834. unidade: 4, dezena: 3, cententa: 8, milhar: 1. --]\n')

numero = input('Digite um número de quatro dígitos: ') 
unidade = numero[3]
dezena = numero[2] 
centena = numero[1] 
milhar = numero[0] 
print('Unidade {}'.format(unidade))
print('dezena {}'.format(dezena))
print('centena {}'.format(centena))
print('milhar {}'.format(milhar))
