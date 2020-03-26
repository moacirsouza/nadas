print("""
048) Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.
""")

somaimpares = 0
for numerosimpares in range (1, 501, 2):
  if numerosimpares % 3 == 0:
    somaimpares += numerosimpares
print('A soma dos ímpares múltiplos de três de 1 até 500 é {}'.format(somaimpares), end=' ')
  






