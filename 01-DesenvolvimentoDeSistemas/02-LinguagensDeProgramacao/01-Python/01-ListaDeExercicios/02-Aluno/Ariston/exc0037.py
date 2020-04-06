print( """\033[1;37;44m [037] Escreva um programa que leia um número inteiro qualquer e peça ao usuário para escolher qual será a base de conversão:
      - 1 para binário
      - 2 para octal
      - 3 para hexadecimal \033[m """)
numero = int(input('Informe um número inteiro: ').strip())

escolhaTipodeConversao = input("""
O número {} pode ser convertido para :
[1] Binária
[2] Octal
[3] Hexadecimal
Escolha sua opção: """.format(numero))

if escolhaTipodeConversao == '1':
      resultado = bin(numero)
      print("para o numero decimal {} temos o seguinte resultado em binario {}".format(numero,resultado))
elif escolhaTipodeConversao == '2':
      resultado = oct(numero)
      print("para o numero decimal {} temos o seguinte resultado em octadecimal {}".format(numero,resultado))
elif escolhaTipodeConversao == '3':
      resultado = hex(numero)
      print("para o numero decimal {} temos o seguinte resultado em hexadecimal {}".format(numero,resultado))
else:
      resultado = '\nVocê escolheu uma opção invalida.'
      print("{}".format(resultado))