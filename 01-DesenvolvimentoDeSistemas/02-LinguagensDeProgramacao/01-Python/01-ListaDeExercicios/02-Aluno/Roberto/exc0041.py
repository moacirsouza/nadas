print("""
041) A Confederação Nacional precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo
com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
""")
anodenascimento = int(input('Digite seu ano de nascimento: ').strip())
anoatual = 2020
idade = anoatual - anodenascimento
print('Sua idade é: {}'.format(idade))
if idade <= 9:
  print('Sua categoria é MIRIM')
elif idade >9 and idade<=14:
  print('Sua categoria é INFANTIL')
elif idade>14 and idade<=19:
  print('Sua categoria é SÊNIOR')
else:
  idade>19
  print('Sua categoria é MASTER') 


