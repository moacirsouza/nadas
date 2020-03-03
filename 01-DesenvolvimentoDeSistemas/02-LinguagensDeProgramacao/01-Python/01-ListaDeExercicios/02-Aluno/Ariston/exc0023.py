print("""
023) Crie um programa em PYTHON que: leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 
Ex: Digite um número: 1834. unidade: 4, dezena: 3, cententa: 8, milhar: 1.
""")
numero=int(input('Digite um numero entre 0 e 9999: '))
milhar = ((numero//1000)%10)
cententa = ((numero//100)%10)
dezena = ((numero//10)%10)
unidade = (numero%10)
print('\nPara o numero: {} temos: \nMilhar é {}\nCentena é {}\nDezena é {}\nUnidade é {}\n'.format(numero,milhar,cententa,dezena,unidade))