print("""
023) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834. unidade: 4, dezena: 3, cententa: 8, milhar: 1. 
""")
### Receber o número como string permite usar apenas um
### 'cast' ao longo do programa ao invés de dois.
numero = input('Digite um número de quatro dígitos: ')

### Método 1: Tratando a entrada como texto ("string")
print('\nTratando a entrada como texto ("string"):')
print('Número:{:>6}'.format(numero))
print('Unidade:{:.>5}'.format(numero[3]))
print('Dezena:{:.>6}'.format(numero[2]))
print('Centena:{:.>5}'.format(numero[1]))
print('Milhar:{:.>6}'.format(numero[0]))

### Método 2: Tratando a entrada como número
numero = int(numero)
milhar = (numero//1000)%10
centena = (numero//100)%10
dezena = (numero//10)%10
unidade = (numero//1)%10

print('\nTratando a entrada como número:')
print('Número:{:>6}'.format(numero))
print('Unidade:{:.>5}'.format(unidade))
print('Dezena:{:.>6}'.format(dezena))
print('Centena:{:.>5}'.format(centena))
print('Milhar:{:.>6}'.format(milhar))
