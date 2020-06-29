print("""
071) Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (Número
inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.
OBS.: Considere que o Caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
""")

### Solução 0: Funcional, mas excessivamente complicada.
# valorDoSaque = []
# valorDoSaque.extend(input('Quanto quer sacar? ').strip()) # Mantido como \
# "string" para aproveitar a propriedade de iterável do objeto
# multiplicador = 1
# notas = ''
# while len(valorDoSaque) != 0:
#     valor = int(valorDoSaque[-1])
#     # Validação da unidade:
#     if multiplicador == 1:
#         if valor < 5:
#             notas += str(valor) \
#                      + ' nota(s) de 1.\n'
#         elif valor > 5:
#             notas += '1 nota de 5 e ' \
#                      + str(valor%5) \
#                      + ' nota(s) de 1.\n'
#         else:
#             notas += '1 nota de 5.\n'
#     # Validação da dezena
#     if multiplicador == 10:
#         if valor == 1:
#             notas += '1 nota de 10.\n'
#         elif 5 > valor >= 2:
#             if valor%2 == 0:
#                 notas += str(valor//2) + \
#                          ' nota(s) de 20.\n'
#             else:
#                 notas += str(valor//2) \
#                          + ' nota(s) de 20 e ' \
#                          + str(valor%2) \
#                          + ' nota(s) de 10\n'
#         elif valor > 5:
#             notas += '1 nota de 50 e '
#             if valor%5 >= 2:
#                 if (valor%5)%2 == 0:
#                     notas += str((valor%5)//2) \
#                              + ' nota(s) de 20.\n'
#                 else:
#                     notas += str((valor%5)//2) \
#                              + ' nota(s) de 20 e ' \
#                              + str((valor%5)//2) \
#                              + ' nota(s) de 10\n'
#             else:
#                 notas += '1 nota de 10.\n'
#         else:
#             notas += '1 nota de 50.\n'
#     # Validação da cententa em diante
#     if multiplicador >= 100:
#         notas += str(valor*multiplicador//50) + ' notas de 50.\n'
#     valorDoSaque.pop()
#     multiplicador *= 10
# print(notas)

### Solução 1: Mais simples que a Solução 0, mas muito deselegante.
### Usa quatro contadores, cria muita repetição de código. Um
### desastre :)
# valorDoSaque = int(input('Quanto quer sacar? '))
# contador50 = contador20 = contador10 = contador1 = 0
# resultado = ''
# while True:
#     if valorDoSaque-50 >= 0:
#         cedula = 50
#         contador50 += 1
#         valorDoSaque -= cedula
#     elif valorDoSaque-20 >= 0:
#         cedula = 20
#         contador20 += 1
#         valorDoSaque -= cedula
#     elif valorDoSaque-10 >= 0:
#         cedula = 10
#         contador10 += 1
#         valorDoSaque -= cedula
#     elif valorDoSaque-1 >=0:
#         cedula = 1
#         contador1 += 1
#         valorDoSaque -= cedula
#     else:
#         if not contador50 == 0:
#             resultado += f'{contador50} cédula(s) de 50\n'
#         if not contador20 == 0:
#             resultado += f'{contador20} cédula(s) de 20.\n'
#         if not contador10 == 0:
#             resultado += f'{contador10} cédula(s) de 10.\n'
#         if not contador1 == 0:
#             resultado += f'{contador1} cédula(s) de 1.\n'
#         break
# print(resultado)

### Solução 2: A mais simples e elegante de todas.
# valorDoSaque = int(input('Quanto quer sacar? R$ '))
# cedula = 50
# contador = 0
# while True:
#     ### [1] O teste só falha quando o valor do saque for menor que o valor
#     ### da cédula que está sendo usada na iteração atual. Ou seja, quando
#     ### a subtração der resultado negativo, significa que é preciso "trocar"
#     ### para a cédula de valor imediatamente inferior, até zerar a variável
#     ### "valorDoSaque", usando as cédulas de R$ 1,00.
#     if valorDoSaque >= cedula:
#         contador += 1
#         valorDoSaque -= cedula
#     else:
#         ### [3] A variável "contador" indica a quantidade de cédulas de cada
#         ### valor a cada iteração. Se este valor for 0, significa que não
#         ### houve contabilização daquela cédula para compor o saque. Como
#         ### não é preciso indicar que zero cédulas de um determinado valor
#         ### serão entregues, só realizamos esta ação, caso contador > 0
#         if contador > 0:
#             print(f'{contador} cédula(s) de {cedula}')
#
#         ### Apenas quando "valorDoSaque" for zero, a operação termina.
#         if valorDoSaque == 0:
#             break
#
#         ### [2] Como elucidado no comentário [1], uma vez que o "else" foi
#         ### alcançado, é preciso alterar o valor da cédula para aquele
#         ### imediatamente inferior, segundo a definição da Regra de
#         ### Negócios. O conjunto de testes a seguir atinge esse propósito.
#         ### Seja qual for o valor da cédula da iteração atual, uma das
#         ### estruturas de controle vai capturá-lo e alterá-lo para próximo.
#         if cedula == 50:
#             cedula = 20
#         elif cedula == 20:
#             cedula = 10
#         elif cedula == 10:
#             cedula = 1
#
#         ### Depois de alterar o valor da cédula, o contaor precisa
#         ### ser zerado, caso contrário, ele acumulará o total do
#         ### grupo anterior de cédulas ao grupo da iteração atual
#         contador = 0

### Solução 3: Desenvolvida pelo colega Emanoel Delfino, entrega uma lógica
### mais elegante em um código enxuto e matematicamente preciso.
### Referência: https://bit.ly/2CKLxVG
print('=' * 35)
print(f'|{"BANCO DO BRASIL":^33}|')
print('=' * 35)
valor = int(input('Qual valor deseja sacar? R$'))
print('=' * 35)

cedulas = [50, 20, 10, 1]

c = 0

while True:
    if valor >= cedulas[c]:
        cedula = cedulas[c]
        totcedulas = valor // cedula
        print(f'Total de {totcedulas:2} cédula(s) de R${cedula:.2f}')
        valor %= cedula
    if valor == 0:
        break
    c += 1

print('=' * 35)
print('Volte sempre ao BANCO DO BRASIL!\nTenha um bom dia!')
print('=' * 35)
